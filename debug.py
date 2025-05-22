from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Create some orders
order1 = Order(alice, espresso, 5.0)
order2 = Order(bob, espresso, 4.5)
order3 = Order(alice, latte, 6.0)

# Test some methods
print(f"{alice.name}'s orders: {len(alice.orders())}")
print(f"{espresso.name} was ordered {espresso.num_orders()} times")
print(f"Average price for {latte.name}: ${latte.average_price():.2f}")

# Test most_aficionado
top_customer = Customer.most_aficionado(espresso)
print(f"Biggest {espresso.name} fan: {top_customer.name if top_customer else 'None'}")