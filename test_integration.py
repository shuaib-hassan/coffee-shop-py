import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestIntegration(unittest.TestCase):
    def test_full_workflow(self):
        # Setup
        customer = Customer("Eve")
        coffee1 = Coffee("Cappuccino")
        coffee2 = Coffee("Flat White")
        
        # Create orders
        order1 = Order(customer, coffee1, 5.0)
        order2 = Order(customer, coffee2, 6.0)
        order3 = Order(customer, coffee1, 5.5)  # Same coffee again
        
        # Verify customer data
        self.assertEqual(len(customer.orders()), 3)
        self.assertEqual(len(customer.coffees()), 2)  # Unique coffees
        
        # Verify coffee data
        self.assertEqual(coffee1.num_orders(), 2)
        self.assertAlmostEqual(coffee1.average_price(), 5.25)
        
        # Verify most_aficionado
        top_customer = Customer.most_aficionado(coffee1)
        self.assertEqual(top_customer.name, "Eve")