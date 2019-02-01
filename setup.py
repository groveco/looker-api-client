# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "looker"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Looker API 3.0 Reference",
    author_email="support@looker.com",
    url="https://looker.com",
    keywords=["Swagger", "Looker API 3.0 Reference"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ### Authorization\n\nThe Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can\ncreate API3 credentials on Looker&#39;s **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to\nobtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests.\nFor details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)\n\n### Client SDKs\n\nThe Looker API is a RESTful system that should be usable by any programming language capable of making\nHTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API&#39;s Swagger\nJSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available\nas an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)\n\n### Try It Out!\n\nThe &#39;api-docs&#39; page served by the Looker instance includes &#39;Try It Out!&#39; buttons for each API method. After logging\nin with API3 credentials, you can use the \&quot;Try It Out!\&quot; buttons to call the API directly from the documentation\npage to interactively explore API features and responses.\n\n### Versioning\n\nFuture releases of Looker will expand this API release-by-release to securely expose more and more of the core\npower of Looker to API client applications. API endpoints marked as \&quot;beta\&quot; may receive breaking changes without\nwarning. Stable (non-beta) API endpoints should not receive breaking changes in future releases.\nFor more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)\n
    """
)


