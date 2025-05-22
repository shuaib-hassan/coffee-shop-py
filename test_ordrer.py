import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave")
        self.coffee = Coffee("Americano")
        self.order = Order(self.customer, self.coffee, 4.0)

    def test_price_validation(self):
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "4.0")  # Not a float
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Too high

    def test_relationships(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertIn(self.order, self.customer.orders())
        self.assertIn(self.order, self.coffee.orders())
        self.assertIn(self.order, Order.all_orders)