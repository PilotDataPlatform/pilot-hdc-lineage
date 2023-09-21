# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from flask_restx import Api

module_api = Api(version='1.0', title='Atlas API',
                 description='Atlas API', doc='/v1/api-doc')

atlas_entity_ns = module_api.namespace(
    'Atlas Entity Actions', description='Operation on Atlas Entity', path='/')

from .audit_operation import AuditAction
from .entity_operation import EntityAction
from .entity_operation import EntityActionByGuid
from .entity_operation import EntityByGuidBulk
from .entity_operation import EntityQueryBasic
from .entity_operation import EntityTagByGuid
from .file_data_operations import FileDataOperations

atlas_entity_ns.add_resource(EntityAction, '/v1/entity')
atlas_entity_ns.add_resource(EntityQueryBasic, '/v1/entity/basic')
atlas_entity_ns.add_resource(EntityByGuidBulk, '/v1/entity/guid/bulk')

atlas_entity_ns.add_resource(EntityActionByGuid, '/v1/entity/guid/<guid>')
atlas_entity_ns.add_resource(EntityTagByGuid, '/v1/entity/guid/<guid>/labels')

atlas_entity_ns.add_resource(AuditAction, '/v1/entity/guid/<guid>/audit')

atlas_entity_ns.add_resource(FileDataOperations, '/v2/filedata')
