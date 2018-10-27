### Python Library for Juspay Express Checkout API

Server side library for interacting with all the JusPay APIs. Ensure that you donot handle any credit/debit card information directly (although this library provides the capability) in your server. Always tokenize the card and then initiate the payment.

#### Dependencies:

The following package is required for this library to work properly.

 * requests (`pip install requests`)

**NOTE**: If `pip` is not installed, install by downloading [get_pip.py](https://bootstrap.pypa.io/get-pip.py) and running the script in your terminal.

#### Installation
You can obtain the latest version of the library directly from python package repository. You don't need to checkout the code unless you need to make any changes to the code directly. If you think the change will help others too, please feel free raise a pull request.  

Run the following command in your terminal:

```bash
pip install --upgrade juspay
```
Simple example for using the library in your project:

```python
import juspay as juspay

# lets configure the environment
juspay.api_key = 'put_your_api_key_here'
juspay.environment = 'production'

# lets create a new order object
my_new_order = juspay.Orders.create(order_id='order_id_100',amount=100.00)
print my_new_order
```
For more information on the APIs and their usage, please refer to the [API documentation](https://www.juspay.in/docs/api/ec).
