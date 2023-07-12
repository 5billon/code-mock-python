from .customer import Customer
from .coffee import Coffee

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
# Order
# Order __init__(self, customer, coffee, price)
#   Orders should be initialized with a customer, coffee, and a price (a number)

# Order property price
#   Returns the price for a coffee
#   Price must be a number between 1 and 10, inclusive
#   raise Exception if setter fails
        
    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if type(new_price) in (int, float) and 1 <= new_price <= 10: # if isinstance(new_price, int) and 1 <= new_price <= 10
            self._price = new_price
        else:
            raise Exception('Range must be within 1 to 10')

    price = property(get_price, set_price)

# Order
# Order property customer
#   Returns the customer object for that order
#   Must be of type Customer
#   raise Exception if setter fails

# Order property coffee
#   Returns the coffee object for that order
#   Must be of type Coffee
#   raise Exception if setter fails

    def get_customer(self):
        return self._customer
    
    def set_customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception('Must be customer instance')

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception('Must be coffee instance')

    coffee = property(get_coffee, set_coffee)