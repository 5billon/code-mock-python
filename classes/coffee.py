class Coffee:
    def __init__(self, name):
        self.name = name

# Coffee
# Coffee __init__(self, name)
#   Coffees should be initialized with a name, as a string

# Coffee property name
#   Returns the coffee's name
#   Should not be able to change after the coffee is created
#   hint: hasattr()
#      if you are using exceptions, uncomment lines 24-25 in coffee_test.py.
#   raise Exception if setter fails
    
    def get_name(self):
        print('testing coffee get')
        return self._name

    def set_name(self, new_name):
        print('testing coffee set')
        if hasattr(self, '_name'):
            raise Exception('Coffee cannot be changed!')
        else:
            self._name = new_name

    name = property(get_name, set_name)

# Coffee
#   Coffee property orders
#       Returns a list of all orders for that coffee
#       orders must be of type Order
#   Coffee property customers
#       Returns a unique list of all customers who have ordered a particular coffee.
#       Customers must be of type Customer
    @property
    def orders(self):
        from classes.order import Order

        coffees_orders = []
        for order in Order.all:
            if order.coffee == self:
                coffees_orders.append(order)
        return coffees_orders

        # orders_list =[]
        # for orders in Order.all:
        #     if orders.coffee == self:
        #         orders_list.append(orders)
        # return orders_list
    
    @property
    def customers(self):
        from classes.customer import Customer

        coffees_customers = []
        for order in self.orders:
            if order.customer not in coffees_customers: # <---- unique list
                coffees_customers.append(order.customer)
        return coffees_customers
        # customers_list = []
        # for customers in Customer.all:
        #     if customers.coffee == self:
        #         customers_list.append(customers)
        # return customers_list

# Coffee
#   Coffee num_orders()
#       eturns the total number of times that coffee has been ordered
#   Coffee average_price()
#       Returns the average price for a coffee based on its orders
#       Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        order_prices = [order.price for order in self.orders]
        sum_prices = sum(order_prices) 
        return sum_prices / self.num_orders()


