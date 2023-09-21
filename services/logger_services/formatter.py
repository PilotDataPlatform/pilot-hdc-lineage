# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from pythonjsonlogger import jsonlogger

from .namespace_declare import service_namespace


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['level'] = record.levelname
        log_record['namespace'] = service_namespace
        log_record['sub_name'] = record.name


def formatter_factory():
    return CustomJsonFormatter(fmt='%(asctime)s %(namespace)s %(sub_name)s %(level)s %(message)s')
