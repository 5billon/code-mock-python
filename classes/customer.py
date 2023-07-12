class Customer:
    def __init__(self, name):
        self.name = name

# Customer
#   Customer __init__(self, name)
#   Customer should be initialized with a name

# Customer property name
#   Return name
#   Names must be of type str
#   Names must be between 1 and 15 characters, inclusive
#   if you are using exceptions, uncomment lines 26-27 and 34-38 in customer_test.py.
#   raise Exception if setter fails
    
    def get_name(self):
        #print('testing')
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str:
            if 1 <= len(new_name) <= 15:
                self._name = new_name
            else:
                raise Exception('Customer name should be between 1 and 15 characters!')
        else:
            raise Exception('Name must be a string')
        #print('testing set')
        self._name = new_name
    name = property(get_name, set_name)

# Customer
#   Customer property orders
#       Returns a list of all orders a customer has ordered
#       orders must be of type Order
#   Customer property coffees
#       Returns a unique list of all coffees a customer has ordered
#       Coffees must be of type Coffee
    @property
    def orders(self):
        from classes.order import Order
        orders_list =[]
        for orders in Order.all:
            if orders.customer == self:
                orders_list.append(orders)
        return orders_list

    @property
    def coffees(self):
        from classes.coffee import Coffee
        coffees_list =[]
        for coffees in Coffee.all:
            if coffees.customer == self:
                coffees_list.append(coffees)
        return coffees_list

# Customer
#   Customer create_order(coffee, price)
#       given a coffee object and a price(as an integer), creates a new order and associates it with that customer and coffee.

    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self, coffee, price)