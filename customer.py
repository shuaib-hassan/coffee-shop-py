class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        coffee_list = []
        for order in self._orders:
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        
        max_spent = 0
        top_customer = None
        
        for customer in cls.all_customers:
            spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if spent > max_spent:
                max_spent = spent
                top_customer = customer
                
        return top_customer