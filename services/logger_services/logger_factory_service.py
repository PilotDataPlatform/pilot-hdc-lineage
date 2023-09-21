# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import logging
import os
import os.path
import sys

from models.meta_class import MetaService

from .formatter import formatter_factory

my_formatter = formatter_factory()


class SrvLoggerFactory(metaclass=MetaService):
    def __init__(self, name):
        if not os.path.exists('./logs/'):
            os.makedirs('./logs/')
        self.name = name

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            handler = logging.FileHandler('logs/{}.log'.format(self.name))
            handler.setFormatter(my_formatter)
            handler.setLevel(logging.DEBUG)
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(my_formatter)
            stdout_handler.setLevel(logging.DEBUG)
            stderr_handler = logging.StreamHandler(sys.stderr)
            stderr_handler.setFormatter(my_formatter)
            stderr_handler.setLevel(logging.ERROR)
            logger.addHandler(handler)
            logger.addHandler(stdout_handler)
            logger.addHandler(stderr_handler)
        return logger
