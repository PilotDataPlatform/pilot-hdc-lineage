# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import requests
from flask import request
from flask_restx import Resource
from requests.auth import HTTPBasicAuth

from app import app
from config import ConfigClass


class AuditAction(Resource):
    def get(self, guid):

        """Get the audit log from entity by guid."""
        count = request.args.get('count', 25)
        app.logger.info('Recieving the parameter: count %s, guid %s', count, guid)

        try:
            headers = {'content-type': 'application/json'}
            res = requests.get(ConfigClass.ATLAS_API + 'api/atlas/v2/entity/%s/audit?count=%d' % (guid, int(count)),
                               verify=False, headers=headers,
                               auth=HTTPBasicAuth(ConfigClass.ATLAS_ADMIN, ConfigClass.ATLAS_PASSWD)
                               )

            if res.status_code >= 300:
                app.logger.error('Error in response: %s', res.text)
                return {'result': res.text}, res.status_code
        except Exception as e:
            app.logger.error('Error in get the audit log: %s', str(e))
            return {'result': str(e)}, 403

        return {'result': res.json()}, res.status_code
