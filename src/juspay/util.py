from . import config
import requests
import juspay
from .JuspayException import *


def check_param(kwargs, string):
    for key, value in kwargs.items():
        if key.startswith(string):
            return True
    return False


def get_arg(kwargs, param):
    if kwargs is None:
        return None
    elif param in kwargs:
        return kwargs[param]
    else:
        return None


def request(method, url, parameters):
    try:
        if juspay.environment == 'production':
            server = 'https://api.juspay.in'
        elif juspay.environment == 'sandbox':
            server = 'https://sandbox.juspay.in'
        else:
            raise Exception("environment variable can only be 'production' or 'sandbox'")
        # Wrapper for requests
        header = {'version': config.api_version,
                  'User-Agent': 'Python SDK'}
        if juspay.merchant_id is not None:
            header['x-merchantid'] = juspay.merchant_id
        if method.upper() == 'GET':
            response = requests.get(server + url, headers=header, params=parameters, auth=(juspay.api_key, ''))
        else:
            response = requests.post(server + url, headers=header, data=parameters, auth=(juspay.api_key, ''))

        # Report error if response is not 200 ("OK")
        if 200 <= response.status_code < 300:
            return response
        elif response.status_code in [400, 404]:
            raise InvalidRequestException(json_body=response.content, http_status=response.status_code,
                                          request_params=parameters)
        elif response.status_code == 401:
            raise AuthenticationException(json_body=response.content, http_status=response.status_code,
                                          request_params=parameters)
        else:
            raise APIException(message="Internal server error. Please contact support@juspay.in.",
                               http_status=response.status_code,
                               request_params=parameters)
    except IOError as err:
        raise APIConnectionException(message=str(err), request_params=parameters)


'''
class list_response:

    def __init__(self, count, offset, total, list):

        self.offset = offset
        self.count = count
        self.total = total
        self.list = list
'''
