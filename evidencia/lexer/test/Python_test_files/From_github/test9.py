class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print("")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break

    def search_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def display_inventory(self):
        if len(self.products) == 0:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product in self.products:
                product.display_info()

# Create the inventory
inventory = Inventory()

# Add products to the inventory
product1 = Product(1, "Laptop", 1200, 5)
product2 = Product(2, "Smartphone", 800, 10)
product3 = Product(3, "Headphones", 100, 20)
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Display the inventory
inventory.display_inventory()

# Search for a product
product_id = 2
product = inventory.search_product(product_id)
if product:
    print(f"Product found:")
    product.display_info()
else:
    print(f"Product with ID {product_id} not found.")

# Remove a product from the inventory
product_id = 1
inventory.remove_product(product_id)

# Display the updated inventory
inventory.display_inventory()
