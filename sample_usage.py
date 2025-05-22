from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
customer1 = Customer("John Doe")
customer2 = Customer("Jane Smith")

# Create some coffees with prices
coffee1 = Coffee("Espresso", price=3.50)
coffee2 = Coffee("Frappuccino", price=5.75)
coffee3 = Coffee("Latte", price=4.25)
coffee4 = Coffee("Cappuccino", price=4.00)

# Create some orders
order1 = Order(customer1, coffee1, quantity=1)
order2 = Order(customer2, coffee2, quantity=2)
order3 = Order(customer1, coffee3, quantity=1)
order4 = Order(customer2, coffee4, quantity=1)

# Print all orders
print("=== Coffee Shop Orders ===")
for order in Order.all_orders:
    print(f"Order: {order}")

# Calculate total sales
total_sales = sum(order.coffee.price * order.quantity for order in Order.all_orders)
print(f"\nTotal Sales: ${total_sales:.2f}")

# Show customer order history
print("\n=== Customer Order History ===")
for customer in [customer1, customer2]:
    customer_total = sum(order.coffee.price * order.quantity 
                        for order in customer.orders())
    print(f"\n{customer.name}'s Orders:")
    for order in customer.orders():
        print(f"- {order}")
    print(f"Total spent: ${customer_total:.2f}")