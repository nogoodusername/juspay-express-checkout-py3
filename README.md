### Python Library for Juspay Express Checkout API

Server side library for interacting with all the JusPay APIs. Ensure that you donot handle any credit/debit card information directly (although this library provides the capability) in your server. Always tokenize the card and then initiate the payment.

#### Dependencies:

The following package is required for this library to work properly.

 * requests (`pip install requests`)

**NOTE**: If `pip` is not installed, install by downloading [get_pip.py](https://bootstrap.pypa.io/get-pip.py) and running the script in your terminal.

#### Installation
Build and install the package using following commands:

```bash
cd src
python3 setup.py dist
pip3 install juspay-1.1.2.tar.gz
```
Simple example for using the library in your project:

```python
import juspay as Juspay

# lets configure the environment
Juspay.api_key = 'put_your_api_key_here'
Juspay.environment = 'production'

# lets create a new order object
my_new_order = Juspay.Orders.create(order_id='order_id_100',amount=100.00)
print(my_new_order)
```
For more information on the APIs and their usage, please refer to the [API documentation](https://www.juspay.in/docs/api/ec).

#### Versions
 * 2016-10-27 - 1.1.2
 * 2018-10-27 - 1.1.3
