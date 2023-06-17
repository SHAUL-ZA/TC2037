class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def display(self):
        print(f"{self.name} - ${self.price}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print()

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display(self):
        print("Menu:")
        print("------")
        for item in self.items:
            item.display()
        print("------")

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def display(self):
        print("Order:")
        print("------")
        for item in self.items:
            print(item.name)
        print("------")
        total = self.calculate_total()
        print(f"Total: ${total}")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.orders = []

    def add_menu_item(self, item):
        self.menu.add_item(item)

    def remove_menu_item(self, item):
        self.menu.remove_item(item)

    def place_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    def display_menu(self):
        self.menu.display()

    def display_orders(self):
        print("Orders:")
        print("-------")
        for i, order in enumerate(self.orders, start=1):
            print(f"Order {i}:")
            order.display()
            print()

    def get_total_revenue(self):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.calculate_total()
        return total_revenue

    def get_most_ordered_item(self):
        item_counts = {}
        for order in self.orders:
            for item in order.items:
                if item.name in item_counts:
                    item_counts[item.name] += 1
                else:
                    item_counts[item.name] = 1
        most_ordered_item = max(item_counts, key=item_counts.get)
        return most_ordered_item

# Create a restaurant
restaurant = Restaurant("The Food Place")

# Create menu items
item1 = MenuItem("Spaghetti Bolognese", 12.99, ["Pasta", "Ground Beef", "Tomato Sauce"])
item2 = MenuItem("Caesar Salad", 8.99, ["Lettuce", "Croutons", "Parmesan Cheese", "Caesar Dressing"])
item3 = MenuItem("Cheeseburger", 9.99, ["Beef Patty", "Cheese", "Lettuce", "Tomato", "Onion", "Pickles", "Bun"])

# Add menu items to the restaurant's menu
restaurant.add_menu_item(item1)
restaurant.add_menu_item(item2)
restaurant.add_menu_item(item3)

# Display the menu
restaurant.display_menu()

# Place orders
order1 = Order()
order1.add_item(item1)
order1.add_item(item2)
restaurant.place_order(order1)

order2 = Order()
order2.add_item(item3)
restaurant.place_order(order2)

# Display the orders
restaurant.display_orders()

# Remove an order
restaurant.remove_order(order1)

# Display the updated orders
restaurant.display_orders()

# Calculate total revenue
total_revenue = restaurant.get_total_revenue()
print(f"Total Revenue: ${total_revenue}")

# Get the most ordered item
most_ordered_item = restaurant.get_most_ordered_item()
print(f"Most Ordered Item: {most_ordered_item}")
