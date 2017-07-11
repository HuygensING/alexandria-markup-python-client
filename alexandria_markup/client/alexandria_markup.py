"""
   Copyright 2017 Huygens ING

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from urllib.parse import urljoin

import requests

from alexandria_markup.client.about_endpoint import AboutEndpoint
from alexandria_markup.client.documents_endpoint import DocumentsEndpoint


class AlexandriaMarkup:
    def __init__(self, server):
        self.server = self.normalized_server(server)
        self.session = requests.Session()
        self.about = AboutEndpoint(self)
        self.documents = DocumentsEndpoint(self)

    @staticmethod
    def normalized_server(server):
        return server if server.endswith('/') else server + '/'

    def get(self, uri):
        url = urljoin(self.server, uri)
        r = self.session.get(url=url)
        r.raise_for_status()
        r.encoding='utf-8'
        return r

    def put(self, uri, data):
        url = urljoin(self.server, uri)
        r = self.session.put(url=url, json=data)
        r.raise_for_status()
        r.encoding='utf-8'
        return r

    def put_data(self, uri, data, content_type='text/plain'):
        url = urljoin(self.server, uri)
        current_content_type = self.session.headers.get('content-type')
        self.session.headers['content-type'] = content_type
        r = self.session.put(url=url, data=data.encode('utf-8'))
        self.session.headers['content-type'] = current_content_type
        r.raise_for_status()
        r.encoding='utf-8'
        return r

    def post(self, uri, json):
        url = urljoin(self.server, uri)
        r = self.session.post(url=url, json=json)
        r.raise_for_status()
        r.encoding='utf-8'
        return r

    def post_data(self, uri, data, content_type='text/plain'):
        url = urljoin(self.server, uri)
        current_content_type = self.session.headers.get('content-type')
        self.session.headers['content-type'] = content_type
        r = self.session.post(url=url, data=data.encode('utf-8'))
        self.session.headers['content-type'] = current_content_type
        r.raise_for_status()
        r.encoding='utf-8'
        return r

    def delete(self, uri):
        r = self.session.delete(url=urljoin(self.server, uri))
        r.raise_for_status()
        r.encoding='utf-8'
        return r
