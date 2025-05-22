from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        customer.orders().append(self)
        coffee.orders().append(self)
        Order.all_orders.append(self)

    def __str__(self):
        return f"Order: {self.coffee.name} for {self.customer.name} at ${self.price:.2f}"

    def __repr__(self):
        return f"Order(customer={self.customer!r}, coffee={self.coffee!r}, price={self.price})"

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value