class Coffee:
    all_coffees = []
    VALID_SIZES = ['small', 'medium', 'large']

    def __init__(self, name, price=0.0, size='medium'):
        self.name = name
        self.price = price
        self.size = size
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(value)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value.lower() not in self.VALID_SIZES:
            raise ValueError(f"Size must be one of {self.VALID_SIZES}")
        self._size = value.lower()

    def orders(self):
        return self._orders

    def customers(self):
        customer_list = []
        for order in self._orders:
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __str__(self):
        return f"{self.size.capitalize()} {self.name} (${self.price:.2f})"