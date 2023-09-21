# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from app import create_app
from config import ConfigClass

app = create_app()

if __name__ == '__main__':
	app.run(host=ConfigClass.host, port=ConfigClass.port, debug=True)
