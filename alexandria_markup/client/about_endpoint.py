from http import HTTPStatus

import alexandria_markup.client.util as util

from alexandria_markup.client.rest_requester import RestRequester
from alexandria_markup.client.alexandria_endpoint import AlexandriaEndpoint


class AboutEndpoint(AlexandriaEndpoint):
    endpoint = 'about'

    def __call__(self):
        return self.get()

    def get(self):
        def getter():
            return self.alexandria.get(self.endpoint)

        return RestRequester(getter).on_status(HTTPStatus.OK, util.entity_as_json).invoke()
