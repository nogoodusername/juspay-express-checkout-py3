# Change Log

## [1.1.6] - 2024-01-25
- added `Merchant ID` param for all the API calls 

## [1.1.5] - 2022-06-07
- added `VPA` class to verify VPA

## [1.1.4] - 2021-12-16
- added coft token fields in cards list api
- fixed order refund api

## [1.1.3] - 2019-10-05
### Added
- client_auth_token to Order

### Changed
- Updated API Version in config.py

## [1.1.2] - 2017-02-27
### Added
- Added payment_method and payment_method_type in order class.
- Added implementation for Wallet create, create_and_authenticate, refresh, authenticate, link & delink.
- Added implementation for get_payment_method in Payments class.
- Added request parameters in error response.
- Updated api_version to 2016-07-19.

## [1.1.1] - 2016-11-14
### Added
- PaymentLink in order, which contains the payment links for an order.
- Order uuid in order creation response.
- API implementation for Customer create, update, and get.
- API implementation for Wallet list and refresh.
- Version in header.

### Change
- API implementation for Order create, update, list, status and refund.
- API implementation for Transaction create.
- API implementation for Card create, list and delete.

