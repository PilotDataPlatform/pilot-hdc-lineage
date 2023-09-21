# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import importlib

from flask import Flask
from flask_cors import CORS
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from config import SRV_NAMESPACE
from config import ConfigClass
from services.logger_services.logger_factory_service import SrvLoggerFactory

app = Flask(__name__)
_main_logger = SrvLoggerFactory('main').get_logger()


def create_app(extra_config_settings={}):
    app.config.from_object(__name__ + '.ConfigClass')
    CORS(
        app,
        origins='*',
        allow_headers=['Content-Type', 'Authorization', 'Access-Control-Allow-Credentials'],
        supports_credentials=True,
        intercept_exceptions=False)

    for apis in ConfigClass.api_modules:
        api = importlib.import_module(apis)
        api.module_api.init_app(app)

    app.logger = _main_logger

    if ConfigClass.opentelemetry_enabled:
        instrument_app(app)

    return app


def instrument_app(app) -> None:
    """Instrument the application with OpenTelemetry tracing."""

    tracer_provider = TracerProvider(resource=Resource.create({SERVICE_NAME: SRV_NAMESPACE}))
    trace.set_tracer_provider(tracer_provider)

    jaeger_exporter = JaegerExporter(
        agent_host_name='127.0.0.1', agent_port=6831
    )

    tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

    FlaskInstrumentor.instrument_app(app)
    RequestsInstrumentor().instrument()
    LoggingInstrumentor().instrument()
