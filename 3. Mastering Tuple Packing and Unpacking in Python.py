def process_orders(orders):
    for index, (customer_name, product, quantity) in enumerate(orders, 1):
        print(f"Order {index}: Customer {customer_name} ordered {quantity} {product}(s)")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Headphones", 3),
    ("David", "Smartphone", 1)
]

# Process and print the orders
process_orders(orders)