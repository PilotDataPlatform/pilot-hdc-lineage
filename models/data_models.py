# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from enum import Enum

from flask_restx import fields

from atlas_api import module_api


class EDataType(Enum):
    nfs_file = 0
    nfs_file_processed = 1
    nfs_file_download = 2


class EPipeline(Enum):
    data_transfer = 1


file_data_post_form = module_api.model(
    'FileDataPostForm',
    {
        'global_entity_id': fields.String(readOnly=True, description='global_entity_id'),
        'uploader': fields.String(readOnly=True, description='uploader'),
        'file_name': fields.String(readOnly=True, description='file name (not include path)'),
        'path': fields.String(readOnly=True, description='path'),
        'file_size': fields.Integer(readOnly=True, description='file size'),
        'description': fields.String(readOnly=True, description='description'),
        'namespace': fields.String(readOnly=True, description='namespace', enum=['greenroom', 'core']),
        'project_code': fields.String(readOnly=True, description='project code'),
        'labels': fields.List(readOnly=True, description='labels', cls_or_instance=fields.String),  # optional
        'processed_pipeline': fields.String(readOnly=True, description='processed_pipeline'),
        'operator': fields.String(readOnly=True, description='operator'),
    },
)
