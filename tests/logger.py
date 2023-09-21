# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import logging
import os
from logging.handlers import RotatingFileHandler


class Logger(object):
    def __init__(self, name='log'):
        if not os.path.exists('./tests/logs/'):
            os.makedirs('./tests/logs/')
        if os.path.isfile('./tests/logs/' + name):
            os.remove('./tests/logs/' + name)
        self.name = name
        self.logger = logging.getLogger(name)
        level = logging.INFO

        self.logger.setLevel(level)
        fh = RotatingFileHandler('./tests/logs/' + name, maxBytes=500000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
