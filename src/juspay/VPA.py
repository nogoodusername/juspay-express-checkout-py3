from . import util
from .JuspayException import InvalidArgumentException


class VPA:

    @staticmethod
    def verify(vpa: str, merchant_id: str, **kwargs):
        params = [
            ('vpa', vpa),
            ('merchant_id', merchant_id),
        ]

        client_auth_token = util.get_arg(kwargs, 'client_auth_token')
        if client_auth_token is not None:
            customer_id = util.get_arg(kwargs, 'customer_id')
            order_id = util.get_arg(kwargs, 'order_id')

            if customer_id is None or order_id is None:
                raise InvalidArgumentException(
                    message='`customer_id` and `order_id` are required while using `client_auth_token`'
                )
            
            params.append(('client_auth_token', client_auth_token))
            params.append(('customer_id', customer_id))
            params.append(('order_id', order_id))

        method = 'POST'
        url = '/v2/upi/verify-vpa'
        response = util.request(method, url, params).json()
        return response
