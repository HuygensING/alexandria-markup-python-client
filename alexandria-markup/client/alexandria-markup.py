import time
from http import HTTPStatus
from urllib.parse import urljoin

import requests

class AlexandriaMarkup:
    def __init__(self, server):
        self.server = self.normalized_server(server)

    def normalized_server(self, server):
        return server if server.endswith('/') else server + '/'