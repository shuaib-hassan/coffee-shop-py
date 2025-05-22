import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Mocha")
        self.customer1 = Customer("Bob")
        self.customer2 = Customer("Charlie")
        self.order1 = Order(self.customer1, self.coffee, 5.5)
        self.order2 = Order(self.customer2, self.coffee, 6.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)  # Not a string
        with self.assertRaises(ValueError):
            Coffee("A")  # Too short

    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertIn(self.order1, self.coffee.orders())

    def test_customers(self):
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 2)
        self.assertIn(self.customer1, customers)

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 5.75)
        # Test with no orders
        new_coffee = Coffee("New")
        self.assertEqual(new_coffee.average_price(), 0)