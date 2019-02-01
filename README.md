## Description
This is a swagger generated Looker API client for Python 2 and 3.

## Requirements
Python 2.7 or later.

## Installation
python setup.py install

## API Generation
Swagger definitions can be exported from Looker directly via [these instructions](https://discourse.looker.com/t/generating-client-sdks-for-the-looker-api/3185).

The API can be generated via the following steps:

1. Checkout swagger-codegen from https://github.com/swagger-api/swagger-codegen with tags/v2.1.6
2. Run the following command, noting the position of the exported lookerapi.json file: `java -jar ./swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i lookerapi.json -l python -o python_sdk`
3. Move the python_sdk/swagger_client to looker and modify the related setup.py accordingly.

Further information is available on Looker's [discussion forum](https://discourse.looker.com/t/generating-client-sdks-for-the-looker-api/3185).
