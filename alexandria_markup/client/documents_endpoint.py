import time
from http import HTTPStatus

import alexandria_markup.client.util as util
from alexandria_markup.client.alexandria_endpoint import AlexandriaEndpoint
from alexandria_markup.client.rest_requester import RestRequester


class DocumentsEndpoint(AlexandriaEndpoint):
    endpoint = 'documents'

    def __init__(self, alexandria):
        super().__init__(alexandria)

    def add(self, lmnl):
        def adder():
            return self.alexandria.post_data(self.endpoint, lmnl, 'text/plain;encoding=utf8')

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.location_as_uuid).invoke()
        return add_result

    def set(self, uuid, lmnl):
        def adder():
            return self.alexandria.put_data(util.endpoint_uri(self.endpoint, uuid), lmnl, 'text/plain;encoding=utf8')

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
