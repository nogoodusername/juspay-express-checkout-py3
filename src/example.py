import juspay
import time

juspay.api_key = '187BF8D543A545789497F14FCAFBD85C'
juspay.environment = 'sandbox'


def dump(obj):
    print "{"
    for attr in dir(obj):
        print "\t%s : %s" % (attr, getattr(obj, attr))
    print "}"


order = juspay.Orders.create(order_id=str(int(time.time())), amount='100.00', currency="INR")

# card = juspay.Cards.create(merchant_id='testmerchant',
#                             customer_id='yourCustId3',
#                             customer_email='a@b.com',
#                             card_number='4242424242424242',
#                             card_exp_year='2019',
#                             card_exp_month='12')

# cards = juspay.Cards.list(customer_id = 'yourCustId3')
# card = juspay.Cards.delete(card_token='<you_card_token>')

# order = juspay.Orders.refund(order_id='1470296153',unique_request_id='unq_1234',amount=10)

# order = juspay.Orders.update(order_id='1470296153', amount='100.00', currency="INR")

# customer = juspay.Customers.create(object_reference_id="yourCustId3", mobile_number="3480239029", email_address="some@some.in", first_name="sdf", last_name="sdfsd")

# customer = juspay.Customers.get(id="yourCustId3")

# customer = juspay.Customers.update(id="yourCustId2", mobile_number="7272727272", email_address="newsome@some.in", first_name="aaa", last_name="ddd")

# customers = juspay.Customers.list(offset="10", count="5")

# wallets = juspay.Wallets.list(order_id="<order_id>")

# wallets = juspay.Wallets.list(customer_id="guest_user_104")

# wallets = juspay.Wallets.refreshBalance(customer_id="<customer_id>")

# payments = juspay.Payments.create_wallet_payment(order_id='<order_id>', merchant_id='testmerchant', payment_method='<MOBIKWIK,PAYTM,FREECHARGE,etc>', redirect_after_payment=True)

# payments = juspay.Payments.create_net_banking_payment(order_id=order.order_id, merchant_id='testmerchant', payment_method='NB_DUMMY', redirect_after_payment=True)

payments = juspay.Payments.create_card_payment(order_id=order.order_id, card_number='4242424242424242',
                                               card_exp_year='2020', card_security_code='123',
                                               card_exp_month='12',
                                               name_on_card='name', merchant_id='testmerchant', save_to_locker=True,
                                               redirect_after_payment=True, payment_method='Maestro')

print 'Success: %r' % order.order_id
order = juspay.Orders.status(order_id = order.order_id)
print dump(order)

print "Payment"
print dump(payments)
print dump(payments.payment.authentication)
# for customer in customers['list']:
#   	dump(customer)



# direct wallet

#customer = juspay.Customers.get(object_reference_id="yourCustId3",
                                   # mobile_number="7272727272",
                                   # email_address="name@domain.in",
                                   # first_name="sdf", last_name="sdfsd")
#
# wallet = juspay.Wallets.create(gateway='MOBIKWIK',
#                                customer_id = customer.id)
# print dump(wallet)

# wallets = juspay.Wallets.list(customer_id="yourCustId3")
#
# wallet = juspay.Wallets.authenticate(wallet_id =wallets[0].id);
# print dump(wallet)

# order = juspay.Orders.create(order_id=str(int(time.time())), amount='1.00', currency="INR",
#                              customer_id='yourCustId1')
#
# print 'Success: %r' % order.order_id
# order = juspay.Orders.status(order_id = order.order_id)
# print dump(order)

# wallet = juspay.Wallets.refresh_by_wallet_id(wallet_id = wallets[0].id)
# dump(wallet)
#
# token = wallets[0].token # use appropriate token
#
# payments = juspay.Payments.create_wallet_payment(order_id=order.order_id,
#                                                  merchant_id='yourMerchantId',
#                                                  redirect_after_payment=True,
#                                                  payment_method='MOBIKWIK',
#                                                  payment_method_type='WALLET',
#                                                  direct_wallet_token=token)
#
# print "Payment"
# print dump(payments)
# print dump(payments.payment.authentication)

# wallet = juspay.Wallets.delink(wallet_id = wallets[0].id)
# print dump(wallet)

# payment methods
#
# payment_methods = juspay.Payments.get_payment_methods(merchant_id = 'yourMerchantId')
#
# for payment_method in payment_methods:
#     print dump(payment_method)
