import json

from middlewares import utils as middlewares_utils

class ConvertKeys:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.body:
            body = json.loads(request.body.decode('utf-8'))
            body = middlewares_utils.camel_to_snake_case(body)
            request._body = json.dumps(body).encode('utf-8')
        response = self.get_response(request)
        return response
