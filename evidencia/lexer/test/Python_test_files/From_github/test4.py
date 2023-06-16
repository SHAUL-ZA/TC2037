class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.price
        return total


def display_menu():
    print("== Welcome to the Online Store ==")
    print("1. Add product to cart")
    print("2. Remove product from cart")
    print("3. View shopping cart")
    print("4. Calculate total")
    print("5. Exit")


def display_products():
    print("== Available Products ==")
    print("1. Shirt - $20")
    print("2. Pants - $30")
    print("3. Shoes - $50")


def run_store():
    cart = ShoppingCart()

    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            display_products()
            selection = input("Select a product: ")

            if selection == "1":
                product = Product("Shirt", 20)
                cart.add_product(product)
                print("Shirt added to cart.")
            elif selection == "2":
                product = Product("Pants", 30)
                cart.add_product(product)
                print("Pants added to cart.")
            elif selection == "3":
                product = Product("Shoes", 50)
                cart.add_product(product)
                print("Shoes added to cart.")
            else:
                print("Invalid selection.")

        elif option == "2":
            if len(cart.items) > 0:
                print("== Products in the cart ==")
                for i, product in enumerate(cart.items):
                    print(f"{i+1}. {product.name} - ${product.price}")

                selection = int(input("Select a product to remove: ")) - 1

                if selection >= 0 and selection < len(cart.items):
                    product_to_remove = cart.items[selection]
                    cart.remove_product(product_to_remove)
                    print(f"{product_to_remove.name} removed from cart.")
                else:
                    print("Invalid selection.")
            else:
                print("The cart is empty.")

        elif option == "3":
            if len(cart.items) > 0:
                print("== Products in the cart ==")
                for i, product in enumerate(cart.items):
                    print(f"{i+1}. {product.name} - ${product.price}")
            else:
                print("The cart is empty.")

        elif option == "4":
            total = cart.calculate_total()
            print(f"The total cost is: ${total}")

        elif option == "5":
            print("Thank you for visiting the Online Store. See you soon!")
            break

        else:
            print("Invalid option. Please select a valid option.")


run_store()
