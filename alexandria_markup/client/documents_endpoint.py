from http import HTTPStatus

import alexandria_markup.client.util as util
from alexandria_markup.client.alexandria_endpoint import AlexandriaEndpoint
from alexandria_markup.client.rest_requester import RestRequester

UTF8TEXT = 'text/plain; encoding=UTF-8'

class DocumentsEndpoint(AlexandriaEndpoint):
    endpoint = 'documents'

    def __init__(self, alexandria):
        super().__init__(alexandria)

    def add_from_lmnl(self, lmnl):
        def adder():
            uri = util.endpoint_uri(self.endpoint, 'lmnl')
            return self.alexandria.post_data(uri, lmnl, UTF8TEXT)

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.location_as_uuid).invoke()
        return add_result

    def add_from_texmecs(self, texmecs):
        def adder():
            uri = util.endpoint_uri(self.endpoint, 'texmecs')
            return self.alexandria.post_data(uri, texmecs, UTF8TEXT)

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.location_as_uuid).invoke()
        return add_result

    def set_from_lmnl(self, uuid, lmnl):
        def adder():
            uri = util.endpoint_uri(self.endpoint, uuid, 'lmnl')
            return self.alexandria.put_data(uri, lmnl, UTF8TEXT)

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.response_as_is).invoke()
        return add_result

    def set_from_texmecs(self, uuid, texmecs):
        def adder():
            uri = util.endpoint_uri(self.endpoint, uuid, 'texmecs')
            return self.alexandria.put_data(uri, texmecs, UTF8TEXT)

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.response_as_is).invoke()
        return add_result

    def lmnl(self, uuid):
        def getter():
            return self.alexandria.get(util.endpoint_uri(self.endpoint, uuid, 'lmnl'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def document_latex(self, uuid):
        def getter():
            return self.alexandria.get(util.endpoint_uri(self.endpoint, uuid, 'latex'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def kdtree_latex(self, uuid):
        def getter():
            return self.alexandria.get(util.endpoint_uri(self.endpoint, uuid, 'kdtree'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def markupdepth_latex(self, uuid):
        def getter():
            return self.alexandria.get(util.endpoint_uri(self.endpoint, uuid, 'markupdepth'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def matrix_latex(self, uuid):
        def getter():
            return self.alexandria.get(util.endpoint_uri(self.endpoint, uuid, 'matrix'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def query(self, uuid, tagql):
        def poster():
            return self.alexandria.post_data(util.endpoint_uri(self.endpoint, uuid, 'query'), tagql)

        return RestRequester(poster).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.json()
