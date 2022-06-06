from . import util


class VPA:

    @staticmethod
    def verify(vpa: str, merchant_id: str):
        params = (
            ('vpa', vpa),
            ('merchant_id', merchant_id),
        )

        method = 'POST'
        url = '/v2/upi/verify-vpa'
        response = util.request(method, url, params).json()
        return response