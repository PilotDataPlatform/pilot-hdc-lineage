# Deprecated

### :no_entry: This repository is no longer supported with the release of Pilot HDC 1.2 :no_entry:

# Lineage Service

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.7](https://img.shields.io/badge/python-3.7-green?style=for-the-badge)](https://www.python.org/)

using Apache Atlas as metadata store to proxy the authorization

The service will running at `<host>:5064`

## Installation

follow the step below to setup the service

### Clone

- Clone this repo to machine using `https://github.com/PilotDataPlatform/lineage.git`

### Setup:

> To run the service as dev mode

```

pip install --no-cache-dir poetry==1.1.12
poetry install
poetry run python app.py
```

> To add new entity in atlas run the curl in the `type.txt` it will add two more entity in atlas:

 - nfs_file
 - nfs_file_processed

## Features:

the service uses the swagger to make the api documents: see the detailed [doc](localhost:6064/v1/api-doc)

### Entity Related API:

 - Add entity to atlas

 - Query entity by the input payload

 - Get entiy by the guid

### Audit Related API:

 - Get audit of entity by guid

## Acknowledgements
The development of the HealthDataCloud open source software was supported by the EBRAINS research infrastructure, funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3) and H2020 Research and Innovation Action Grant Interactive Computing E-Infrastructure for the Human Brain Project ICEI 800858.
