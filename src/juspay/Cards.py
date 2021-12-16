from . import util
from .JuspayException import InvalidArgumentException


class Cards:

    def __init__(self):
        return

    class Card:

        class COFTToken:
            def __init__(self, kwargs):
                self.card_reference = util.get_arg(kwargs, 'card_reference'),
                self.last_four_digits = util.get_arg(kwargs, 'last_four_digits')
                self.card_fingerprint = util.get_arg(kwargs, 'card_fingerprint')
                self.card_isin = util.get_arg(kwargs, 'card_isin')
                self.expiry_month = util.get_arg(kwargs, 'expiry_month')
                self.expiry_year = util.get_arg(kwargs, 'expiry_year')
                self.par = util.get_arg(kwargs, 'par')
                self.tokenization_status = util.get_arg(kwargs, 'tokenization_status')

        def __init__(self, kwargs):
            self.token = util.get_arg(kwargs, 'card_token')
            self.reference = util.get_arg(kwargs, 'card_reference')
            self.number = util.get_arg(kwargs, 'card_number')
            self.isin = util.get_arg(kwargs, 'card_isin')
            self.exp_year = util.get_arg(kwargs, 'card_exp_year')
            self.exp_month = util.get_arg(kwargs, 'card_exp_month')
            self.type = util.get_arg(kwargs, 'card_type')
            self.issuer = util.get_arg(kwargs, 'card_issuer')
            self.brand = util.get_arg(kwargs, 'card_brand')
            self.nickname = util.get_arg(kwargs, 'nickname')
            self.name = util.get_arg(kwargs, 'name_on_card')
            self.expired = util.get_arg(kwargs, 'expired')
            self.fingerprint = util.get_arg(kwargs, 'card_fingerprint')
            self.juspay_bank_code = util.get_arg(kwargs, 'juspay_bank_code')
            self.card_sub_type = util.get_arg(kwargs, 'card_sub_type')
            self.card_issuer_country = util.get_arg(kwargs, 'card_issuer_country')
            self.tokenize_support = util.get_arg(kwargs, 'tokenize_support')
            self.provider_category = util.get_arg(kwargs, 'provider_category')
            self.provider = util.get_arg(kwargs, 'provider')
            if util.get_arg(kwargs, 'token') is not None:
                self.coft_token = Cards.Card.COFTToken(util.get_arg(kwargs, 'token'))
            else:
                self.coft_token = None
            self.deleted = util.get_arg(kwargs, 'deleted')

    @staticmethod
    def create(**kwargs):
        if kwargs is None or len(kwargs) == 0:
            raise InvalidArgumentException()

        method = 'POST'
        url = '/card/add'
        response = util.request(method, url, kwargs).json()
        card = Cards.Card(response)
        return card

    @staticmethod
    def list(**kwargs):
        customer_id = util.get_arg(kwargs,'customer_id')
        if customer_id is None:
            raise InvalidArgumentException('`customer_id` is a required argument for Cards.list()\n')

        method = 'GET'
        url = '/card/list'
        response = util.request(method, url, kwargs).json()
        response = util.get_arg(response, 'cards')
        cards = []
        if response is not None:
            for card in response:
                card = Cards.Card(card)
                cards.append(card)
        return cards

    @staticmethod
    def delete(**kwargs):
        card_token = util.get_arg(kwargs,'card_token')
        if card_token is None:
            raise InvalidArgumentException('`card_token` is a required argument for Cards.delete()\n')

        method = 'POST'
        url = '/card/delete'
        response = util.request(method, url, kwargs).json()
        card = Cards.Card(response)
        return card
