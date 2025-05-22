import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")
        self.order1 = Order(self.customer, self.coffee1, 5.0)
        self.order2 = Order(self.customer, self.coffee2, 4.5)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)  # Not a string
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("ThisNameIsWayTooLong")  # >15 chars

    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 2)
        self.assertIn(self.order1, self.customer.orders())

    def test_coffees(self):
        coffees = self.customer.coffees()
        self.assertEqual(len(coffees), 2)
        self.assertIn(self.coffee1, coffees)

    def test_create_order(self):
        new_order = self.customer.create_order(self.coffee1, 6.0)
        self.assertIn(new_order, self.customer.orders())
        self.assertEqual(new_order.price, 6.0)

    def test_most_aficionado(self):
        big_spender = Customer("Big Spender")
        Order(big_spender, self.coffee1, 10.0)
        Order(big_spender, self.coffee1, 10.0)
        
        top_customer = Customer.most_aficionado(self.coffee1)
        self.assertEqual(top_customer.name, "Big Spender")