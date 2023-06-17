# Time:  O(n^3)
# Space: O(1)

import collections


# Two pointer solution. (1356ms)
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in xrange(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1
        return result


# Time:  O(n^2 * p)
# Space: O(n^2 * p)
# Hash solution. (224ms)
class Solution2(object):
    def fourSum(self, nums, target):
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in xrange(2, len(nums)):
            for d in xrange(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(str(quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result


# Time:  O(n^2 * p) ~ O(n^4)
# Space: O(n^2)
class Solution3(object):
    def fourSum(self, nums, target):
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                           b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)


# This code is used for educational purposes only and was made by 

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def find132pattern(self, nums):
        ak = float("-inf")
        stk = []
        for i in reversed(xrange(len(nums))):
            if nums[i] < ak:
                return True
            while stk and stk[-1] < nums[i]:
                ak = stk.pop()
            stk.append(nums[i])
        return False


# Time:  O(n^2)
# Space: O(1)
class Solution_TLE(object):
    def find132pattern(self, nums):
    
        for k in xrange(len(nums)):
            valid = False
            for j in xrange(k):
                if nums[j] < nums[k]:
                    valid = True
                elif nums[j] > nums[k]:
                    if valid:
                        return True
        return False
    

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        # p(k) = 1 * (prob that 1th passenger takes his own seat) +
        #        0 * (prob that 1th passenger takes kth one's seat) +
        #        1 * (prob that 1th passenger takes the others' seat) * 
        #            (prob that the first k-1 passengers get a seat
        #             which is not kth one's seat)
        #      = 1/k + p(k-1)*(k-2)/k
        #
        # p(1) = 1
        # p(2) = 1/2 + p(1) * (2-2)/2 = 1/2
        # p(3) = 1/3 + p(2) * (3-2)/3 = 1/3 + 1/2 * (3-2)/3 = 1/2
        # ...
        # p(n) = 1/n + 1/2 * (n-2)/n = (2+n-2)/(2n) = 1/2
        return 0.5 if n != 1 else 1.0

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def nthPersonGetsNthSeat(self, n):
        dp = [0.0]*2
        dp[0] = 1.0  # zero-indexed
        for i in xrange(2, n+1):
            dp[(i-1)%2] = 1.0/i+dp[(i-2)%2]*(i-2)/i
        return dp[(n-1)%2]

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


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, task, new_title, new_description, new_due_date):
        task.title = new_title
        task.description = new_description
        task.due_date = new_due_date

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("== Tasks ==")
        for task in self.tasks:
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print("---------------------")

def display_menu():
    print("== Task Manager Menu ==")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def run_task_manager():
    task_manager = TaskManager()

    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            due_date = input("Enter the task due date: ")
            task = Task(title, description, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif option == "2":
            title = input("Enter the title of the task to remove: ")
            task = task_manager.get_task(title)
            if task:
                task_manager.remove_task(task)
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif option == "3":
            title = input("Enter the title of the task to update: ")
            task = task_manager.get_task(title)
            if task:
                new_title = input("Enter the new title: ")
                new_description = input("Enter the new description: ")
                new_due_date = input("Enter the new due date: ")
                task_manager.update_task(task, new_title, new_description, new_due_date)
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif option == "4":
            task_manager.display_tasks()

        elif option == "5":
            print("Exiting the Task Manager.")
            break

        else:
            print("Invalid option. Please select a valid option.")

run_task_manager()

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def update_student(self, student, name, age, grade):
        student.name = name
        student.age = age
        student.grade = grade

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        print("== Student Registry ==")
        for student in self.students:
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print("---------------------")

def display_menu():
    print("== Student Registry Menu ==")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Search Student by ID")
    print("6. Exit")

def run_student_registry():
    student_registry = StudentRegistry()

    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            student_id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            grade = input("Enter the student grade: ")
            student = Student(student_id, name, age, grade)
            student_registry.add_student(student)
            print("Student added successfully.")

        elif option == "2":
            student_id = input("Enter the student ID to remove: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                student_registry.remove_student(student)
                print("Student removed successfully.")
            else:
                print("Student not found.")

        elif option == "3":
            student_id = input("Enter the student ID to update: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                name = input("Enter the new name: ")
                age = input("Enter the new age: ")
                grade = input("Enter the new grade: ")
                student_registry.update_student(student, name, age, grade)
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif option == "4":
            student_registry.display_students()

        elif option == "5":
            student_id = input("Enter the student ID to search: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                print("Student found:")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
            else:
                print("Student not found.")

        elif option == "6":
            print("Exiting the Student Registry.")
            break

        else:
            print("Invalid option. Please select a valid option.")

run_student_registry()


class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s):")
            for contact in found_contacts:
                print_contact(contact)
        else:
            print("No matching contacts found.")

    def edit_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s).")
            print("Select a contact to edit:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact.name}")
            choice = int(input("Enter the contact number: ")) - 1
            if 0 <= choice < len(found_contacts):
                contact = found_contacts[choice]
                print("Enter new details for the contact:")
                contact.name = input("Name: ")
                contact.phone_number = input("Phone Number: ")
                contact.email = input("Email: ")
                print(f"Contact '{contact.name}' updated successfully.")
            else:
                print("Invalid contact number.")
        else:
            print("No matching contacts found.")

    def delete_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s).")
            print("Select a contact to delete:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact.name}")
            choice = int(input("Enter the contact number: ")) - 1
            if 0 <= choice < len(found_contacts):
                contact = found_contacts[choice]
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
            else:
                print("Invalid contact number.")
        else:
            print("No matching contacts found.")

    def display_contacts(self):
        if self.contacts:
            print("Address Book:")
            for contact in self.contacts:
                print_contact(contact)
        else:
            print("Address Book is empty.")

def print_contact(contact):
    print(f"Name: {contact.name}")
    print(f"Phone Number: {contact.phone_number}")
    print(f"Email: {contact.email}")
    print()

def main():
    address_book = AddressBook()

    while True:
        print("Address Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter contact details:")
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)
        elif choice == "2":
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif choice == "3":
            name = input("Enter name to edit: ")
            address_book.edit_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            address_book.delete_contact(name)
        elif choice == "5":
            address_book.display_contacts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import random

# Card and Deck Classes

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Player and Game Classes

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        total_value = 0
        ace_count = 0
        for card in self.hand:
            if card.rank.isdigit():
                total_value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                total_value += 10
            elif card.rank == 'A':
                total_value += 11
                ace_count += 1
        while total_value > 21 and ace_count > 0:
            total_value -= 10
            ace_count -= 1
        return total_value

    def display_hand(self, show_all_cards=False):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            if show_all_cards:
                print(card)
            else:
                print("Hidden Card")
        print("")

def play_blackjack():
    print("Welcome to Blackjack!")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards are worth 10. Aces are worth 1 or 11.")

    player_name = input("Enter your name: ")
    player = Player(player_name)
    dealer = Player("Dealer")

    deck = Deck()
    deck.shuffle_deck()

    # Deal initial cards
    player.draw_card(deck.deal_card())
    dealer.draw_card(deck.deal_card())
    player.draw_card(deck.deal_card())
    dealer.draw_card(deck.deal_card())

    # Show player's hand and one of the dealer's cards
    player.display_hand()
    dealer.display_hand(show_all_cards=False)

    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").lower()

        if choice == "h":
            player.draw_card(deck.deal_card())
            player.display_hand()
            if player.get_hand_value() > 21:
                print("Bust! You lose.")
                return
        elif choice == "s":
            break
        else:
            print("Invalid choice. Please try again.")

    # Dealer's turn
    dealer.display_hand(show_all_cards=True)
    while dealer.get_hand_value() < 17:
        dealer.draw_card(deck.deal_card())
        dealer.display_hand(show_all_cards=True)
        if dealer.get_hand_value() > 21:
            print("Dealer busts! You win.")
            return

    # Compare hands and determine the winner
    player_value = player.get_hand_value()
    dealer_value = dealer.get_hand_value()

    if player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Start the game
play_blackjack()


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


import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.experience = 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Experience: {self.experience}")
        print("")

    def level_up(self):
        self.level += 1
        self.health += random.randint(5, 10)
        self.attack += random.randint(1, 3)
        self.defense += random.randint(1, 3)
        print(f"{self.name} leveled up to level {self.level}!")

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gained {experience} experience points!")

class Enemy:
    def __init__(self, name, health, attack, defense, experience):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience

    def display_info(self):
        print(f"Enemy: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Experience: {self.experience}")
        print("")

    def take_damage(self, damage):
        actual_damage = damage - self.defense
        if actual_damage > 0:
            self.health -= actual_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            return True
        return False

class RPGGame:
    def __init__(self):
        self.player = None
        self.enemies = [
            Enemy("Goblin", 20, 5, 2, 10),
            Enemy("Skeleton", 30, 7, 3, 15),
            Enemy("Orc", 40, 9, 5, 20)
        ]

    def start_game(self):
        print("Welcome to the RPG Game!")
        self.create_character()

    def create_character(self):
        name = input("Enter your character name: ")
        health = random.randint(50, 100)
        attack = random.randint(10, 15)
        defense = random.randint(5, 10)
        self.player = Character(name, health, attack, defense)
        print("Character created successfully!")
        self.play_game()

    def play_game(self):
        while True:
            print("\n-------- MENU --------")
            print("1. Display Character Info")
            print("2. Battle Enemy")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.player.display_info()
            elif choice == "2":
                self.battle_enemy()
            elif choice == "3":
                print("Exiting the game...")
                break
            else:
                print("Invalid choice. Please try again.")

    def battle_enemy(self):
        enemy = random.choice(self.enemies)
        print(f"\nYou encountered an {enemy.name}!")
        print("-------- BATTLE --------")
        enemy.display_info()
        print("------------------------")

        while True:
            print("\n-------- BATTLE MENU --------")
            print("1. Attack")
            print("2. Run")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.attack_enemy(enemy)
                if enemy.health <= 0:
                    self.player.gain_experience(enemy.experience)
                    self.check_level_up()
                    break
                self.enemy_attack()
                if self.player.health <= 0:
                    print("Game over! You were defeated.")
                    break
            elif choice == "2":
                print("You ran away from the battle.")
                break
            else:
                print("Invalid choice. Please try again.")

    def attack_enemy(self, enemy):
        damage = self.player.attack + random.randint(1, 3)
        print(f"You attacked the {enemy.name} and dealt {damage} damage.")
        enemy.take_damage(damage)

    def enemy_attack(self):
        enemy = random.choice(self.enemies)
        damage = enemy.attack + random.randint(1, 3)
        print(f"The {enemy.name} attacked you and dealt {damage} damage.")
        self.player.health -= damage

    def check_level_up(self):
        if self.player.experience >= 50 * self.player.level:
            self.player.level_up()

game = RPGGame()
game.start_game()


import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 4, figsize=(12, 12))

# Draw a circle
circle = plt.Circle((0.5, 0.5), 0.4, color='blue', alpha=0.5)
axs[0, 0].add_patch(circle)
axs[0, 0].set_aspect('equal')
axs[0, 0].set_xlim(0, 1)
axs[0, 0].set_ylim(0, 1)
axs[0, 0].set_title('Circle')

# Draw a rectangle
rectangle = plt.Rectangle((0.2, 0.2), 0.6, 0.4, color='red', alpha=0.5)
axs[0, 1].add_patch(rectangle)
axs[0, 1].set_aspect('equal')
axs[0, 1].set_xlim(0, 1)
axs[0, 1].set_ylim(0, 1)
axs[0, 1].set_title('Rectangle')

# Draw an ellipse
ellipse = plt.Ellipse((0.5, 0.5), 0.6, 0.4, angle=45, color='green', alpha=0.5)
axs[0, 2].add_patch(ellipse)
axs[0, 2].set_aspect('equal')
axs[0, 2].set_xlim(0, 1)
axs[0, 2].set_ylim(0, 1)
axs[0, 2].set_title('Ellipse')

# Draw a triangle
triangle = plt.Polygon([[0.3, 0.7], [0.7, 0.7], [0.5, 0.3]], color='purple', alpha=0.5)
axs[0, 3].add_patch(triangle)
axs[0, 3].set_aspect('equal')
axs[0, 3].set_xlim(0, 1)
axs[0, 3].set_ylim(0, 1)
axs[0, 3].set_title('Triangle')

# Draw a pentagon
pentagon = plt.Polygon([[0.3, 0.8], [0.7, 0.8], [0.8, 0.6], [0.5, 0.2], [0.2, 0.6]], color='orange', alpha=0.5)
axs[1, 0].add_patch(pentagon)
axs[1, 0].set_aspect('equal')
axs[1, 0].set_xlim(0, 1)
axs[1, 0].set_ylim(0, 1)
axs[1, 0].set_title('Pentagon')

# Draw a star
star = plt.Polygon([[0.5, 0.9], [0.63, 0.6], [0.95, 0.6], [0.68, 0.4], [0.8, 0.1],
                    [0.5, 0.3], [0.2, 0.1], [0.32, 0.4], [0.05, 0.6], [0.37, 0.6]],
                   color='brown', alpha=0.5)
axs[1, 1].add_patch(star)
axs[1, 1].set_aspect('equal')
axs[1, 1].set_xlim(0, 1)
axs[1, 1].set_ylim(0, 1)
axs[1, 1].set_title('Star')

# Draw an arrow
arrow = plt.Arrow(0.2, 0.5, 0.6, 0.2, width=0.1, color='magenta')
axs[1, 2].add_patch(arrow)
axs[1, 2].set_aspect('equal')
axs[1, 2].set_xlim(0, 1)
axs[1, 2].set_ylim(0, 1)
axs[1, 2].set_title('Arrow')

# Draw a hexagon
hexagon = plt.Polygon([[0.3, 0.8], [0.7, 0.8], [0.9, 0.5], [0.7, 0.2], [0.3, 0.2], [0.1, 0.5]],
                      color='cyan', alpha=0.5)
axs[1, 3].add_patch(hexagon)
axs[1, 3].set_aspect('equal')
axs[1, 3].set_xlim(0, 1)
axs[1, 3].set_ylim(0, 1)
axs[1, 3].set_title('Hexagon')

# Draw an octagon
octagon = plt.Polygon([[0.3, 0.7], [0.7, 0.7], [0.9, 0.5], [0.9, 0.1], [0.7, 0.3], [0.3, 0.3], [0.1, 0.5], [0.1, 0.9]],
                      color='lime', alpha=0.5)
axs[2, 0].add_patch(octagon)
axs[2, 0].set_aspect('equal')
axs[2, 0].set_xlim(0, 1)
axs[2, 0].set_ylim(0, 1)
axs[2, 0].set_title('Octagon')

# Draw a trapezoid
trapezoid = plt.Polygon([[0.2, 0.8], [0.8, 0.8], [0.7, 0.5], [0.3, 0.5]], color='yellow', alpha=0.5)
axs[2, 1].add_patch(trapezoid)
axs[2, 1].set_aspect('equal')
axs[2, 1].set_xlim(0, 1)
axs[2, 1].set_ylim(0, 1)
axs[2, 1].set_title('Trapezoid')

# Draw a diamond
diamond = plt.Polygon([[0.5, 0.9], [0.75, 0.5], [0.5, 0.1], [0.25, 0.5]], color='pink', alpha=0.5)
axs[2, 2].add_patch(diamond)
axs[2, 2].set_aspect('equal')
axs[2, 2].set_xlim(0, 1)
axs[2, 2].set_ylim(0, 1)
axs[2, 2].set_title('Diamond')

# Draw a cross
cross = plt.Polygon([[0.4, 0.8], [0.6, 0.8], [0.6, 0.6], [0.8, 0.6], [0.8, 0.4], [0.6, 0.4],
                     [0.6, 0.2], [0.4, 0.2], [0.4, 0.4], [0.2, 0.4], [0.2, 0.6], [0.4, 0.6]],
                    color='gray', alpha=0.5)
axs[2, 3].add_patch(cross)
axs[2, 3].set_aspect('equal')
axs[2, 3].set_xlim(0, 1)
axs[2, 3].set_ylim(0, 1)
axs[2, 3].set_title('Cross')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

import math

# Function to calculate the Fibonacci sequence up to a given limit
def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Function to calculate the nth prime number
def nth_prime_number(n):
    primes = [2]
    number = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 2
    return primes[-1]

# Function to calculate the sum of digits in a factorial number
def factorial_digit_sum(n):
    factorial = math.factorial(n)
    digit_sum = sum(int(digit) for digit in str(factorial))
    return digit_sum

# Function to calculate the nth term of the geometric series
def geometric_series_term(a, r, n):
    term = a * math.pow(r, n-1)
    return term

# Function to calculate the sum of an arithmetic series
def arithmetic_series_sum(a, d, n):
    last_term = a + (n - 1) * d
    series_sum = (n * (a + last_term)) / 2
    return series_sum

# Examples using the functions
fibonacci_limit = 100
fibonacci = fibonacci_sequence(fibonacci_limit)
print("Fibonacci sequence up to", fibonacci_limit, ":", fibonacci)

nth_prime = 10
nth_prime_number = nth_prime_number(nth_prime)
print("The", nth_prime, "prime number is:", nth_prime_number)

factorial_number = 5
factorial_sum = factorial_digit_sum(factorial_number)
print("Sum of digits in", factorial_number, "factorial:", factorial_sum)

a = 2
r = 3
n = 4
geometric_term = geometric_series_term(a, r, n)
print("The", n, "term of the geometric series is:", geometric_term)

a_arithmetic = 3
d_arithmetic = 2
n_arithmetic = 5
arithmetic_sum = arithmetic_series_sum(a_arithmetic, d_arithmetic, n_arithmetic)
print("Sum of the arithmetic series:", arithmetic_sum)

import random

# Function to roll a 6-sided die
def roll_die():
    return random.randint(1, 6)

# Function to move the player to a new position
def move_player(player, steps):
    new_position = player + steps
    return new_position

# Function to check if the player has won
def has_won(player):
    return player >= 100

# Board with snakes and ladders
board = {
    4: 14,
    9: 31,
    17: 7,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    54: 34,
    62: 19,
    63: 81,
    64: 60,
    71: 91,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

# Initial positions of the players
player1 = 0
player2 = 0

# Main game loop
while True:
    # Player 1's turn
    print("Player 1, it's your turn.")
    input("Press Enter to roll the die...")
    roll = roll_die()
    print("You rolled a", roll)
    player1 = move_player(player1, roll)

    # Check if Player 1 landed on a snake or ladder
    if player1 in board:
        new_position = board[player1]
        if new_position > player1:
            print("Ladder! You advance to position", new_position)
        else:
            print("Snake! You slide down to position", new_position)
        player1 = new_position

    # Check if Player 1 has won
    if has_won(player1):
        print("Congratulations! Player 1 has won the game.")
        break

    # Player 2's turn
    print("Player 2, it's your turn.")
    input("Press Enter to roll the die...")
    roll = roll_die()
    print("You rolled a", roll)
    player2 = move_player(player2, roll)

    # Check if Player 2 landed on a snake or ladder
    if player2 in board:
        new_position = board[player2]
        if new_position > player2:
            print("Ladder! You advance to position", new_position)
        else:
            print("Snake! You slide down to position", new_position)
        player2 = new_position

    # Check if Player 2 has won
    if has_won(player2):
        print("Congratulations! Player 2 has won the game.")
        break


import random

# List of words for the Hangman game
words = ["python", "programming", "computer", "game", "development", "application", "code", "algorithm"]

# Function to select a random word from the list
def select_word():
    return random.choice(words)

# Function to hide the word with underscores
def hide_word(word):
    return "_" * len(word)

# Function to display the hidden word with guessed letters
def show_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()

# Function to check if the letter is in the word
def check_letter(word, letter):
    return letter in word

# Function to display the current state of the hangman drawing
def show_hangman(remaining_attempts):
    hangman = [
        "   _______",
        "  |       |",
        "  |       " + ("O" if remaining_attempts < 6 else ""),
        "  |      " + ("/|" if remaining_attempts < 5 else "/|\ "),
        "  |       " + ("|" if remaining_attempts < 4 else "|"),
        "  |      " + ("/" if remaining_attempts < 3 else "/ \ "),
        " _|_"
    ]
    for line in hangman:
        print(line)

# Hangman Game
def play_hangman():
    secret_word = select_word()
    hidden_word = hide_word(secret_word)
    guessed_letters = []
    remaining_attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(secret_word), "letters.")

    while remaining_attempts > 0:
        print("\nWord:", show_word(secret_word, guessed_letters))
        print("Remaining attempts:", remaining_attempts)
        show_hangman(remaining_attempts)

        letter = input("Enter a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single valid letter.")
            continue

        if letter in guessed_letters:
            print("You've already guessed that letter. Try another one.")
            continue

        if check_letter(secret_word, letter):
            guessed_letters.append(letter)
            if hidden_word == secret_word:
                print("\nCongratulations! You've guessed the word:", secret_word)
                break
        else:
            print("The letter is not in the word.")
            remaining_attempts -= 1

    if remaining_attempts == 0:
        show_hangman(remaining_attempts)
        print("\nYou've lost! The word was:", secret_word)

# Start the Hangman game
play_hangman()

# Tic-Tac-Toe Game

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def check_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"

    while True:
        display_board(board)

        print("Player", current_player + "'s turn.")
        print("Enter the row (0-2) and column (0-2) separated by space:")

        move = input().split()
        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print("Invalid input. Try again.")
            continue

        row = int(move[0])
        col = int(move[1])

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row and column should be in the range 0-2. Try again.")
            continue

        if board[row][col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print("Player", current_player, "wins!")
            break

        if check_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_tic_tac_toe()
    else:
        print("Thank you for playing Tic-Tac-Toe!")

# Start the Tic-Tac-Toe game
play_tic_tac_toe()


import math

# Function to calculate the area of a square
def calculate_square_area(side):
    area = side ** 2
    return area

# Function to calculate the perimeter of a square
def calculate_square_perimeter(side):
    perimeter = 4 * side
    return perimeter

# Function to calculate the area of a triangle using Heron's formula
def calculate_triangle_area_heron(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    return area

# Function to calculate the area of a triangle using base and height
def calculate_triangle_area_base_height(base, height):
    area = 0.5 * base * height
    return area

# Function to calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

# Function to calculate the area of a parallelogram
def calculate_parallelogram_area(base, height):
    area = base * height
    return area

# Function to calculate the perimeter of a parallelogram
def calculate_parallelogram_perimeter(side1, side2):
    perimeter = 2 * (side1 + side2)
    return perimeter

# Function to calculate the area of a trapezoid
def calculate_trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Function to calculate the perimeter of a trapezoid
def calculate_trapezoid_perimeter(base1, base2, side1, side2):
    perimeter = base1 + base2 + side1 + side2
    return perimeter

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Function to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

# Function to calculate the surface area of a sphere
def calculate_sphere_surface_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

# Function to calculate the area of a cylinder
def calculate_cylinder_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

# Function to calculate the area of a cone
def calculate_cone_area(radius, slant_height):
    base_area = math.pi * radius ** 2
    lateral_area = math.pi * radius * slant_height
    area = base_area + lateral_area
    return area

# Function to calculate the volume of a cone
def calculate_cone_volume(radius, height):
    volume = (1 / 3) * math.pi * radius ** 2 * height
    return volume

# Perform various mathematical calculations
side = 5
square_area = calculate_square_area(side)
square_perimeter = calculate_square_perimeter(side)

side1 = 3
side2 = 4
side3 = 5
triangle_area_heron = calculate_triangle_area_heron(side1, side2, side3)
triangle_area_base_height = calculate_triangle_area_base_height(side1, side2)
triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)

base = 6
height = 8
parallelogram_area = calculate_parallelogram_area(base, height)
parallelogram_perimeter = calculate_parallelogram_perimeter(side1, side2)

base1 = 5
base2 = 7
trapezoid_height = 4
trapezoid_area = calculate_trapezoid_area(base1, base2, trapezoid_height)
trapezoid_perimeter = calculate_trapezoid_perimeter(base1, base2, side1, side2)

radius = 4
circle_area = calculate_circle_area(radius)
circle_circumference = calculate_circle_circumference(radius)

sphere_volume = calculate_sphere_volume(radius)
sphere_surface_area = calculate_sphere_surface_area(radius)

cylinder_height = 10
cylinder_area = calculate_cylinder_area(radius, cylinder_height)
cylinder_volume = calculate_cylinder_volume(radius, cylinder_height)

cone_slant_height = 9
cone_area = calculate_cone_area(radius, cone_slant_height)
cone_volume = calculate_cone_volume(radius, cylinder_height)

# Print the results
print("Square - Side:", side)
print("Square Area:", square_area)
print("Square Perimeter:", square_perimeter)

print("\nTriangle (Heron's formula) - Side1:", side1, "Side2:", side2, "Side3:", side3)
print("Triangle Area (Heron's formula):", triangle_area_heron)
print("Triangle Area (Base and Height):", triangle_area_base_height)
print("Triangle Perimeter:", triangle_perimeter)

print("\nParallelogram - Base:", base, "Height:", height)
print("Parallelogram Area:", parallelogram_area)
print("Parallelogram Perimeter:", parallelogram_perimeter)

print("\nTrapezoid - Base1:", base1, "Base2:", base2, "Height:", trapezoid_height)
print("Trapezoid Area:", trapezoid_area)
print("Trapezoid Perimeter:", trapezoid_perimeter)

print("\nCircle - Radius:", radius)
print("Circle Area:", circle_area)
print("Circle Circumference:", circle_circumference)

print("\nSphere - Radius:", radius)
print("Sphere Volume:", sphere_volume)
print("Sphere Surface Area:", sphere_surface_area)

print("\nCylinder - Radius:", radius, "Height:", cylinder_height)
print("Cylinder Area:", cylinder_area)
print("Cylinder Volume:", cylinder_volume)

print("\nCone - Radius:", radius, "Slant Height:", cone_slant_height)
print("Cone Area:", cone_area)
print("Cone Volume:", cone_volume)


# Loop to print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Loop to calculate the sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)

# Loop to print the multiplication table of a number
num = 5
print("Multiplication table of", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Loop to print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i)

# Loop to find the factorial of a number
num = 6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)

# Loop to check if a number is prime
num = 17
is_prime = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break
print(num, "is prime:", is_prime)

# Loop to generate a Fibonacci sequence
num_terms = 10
fibonacci_seq = [0, 1]
for i in range(2, num_terms):
    next_term = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
    fibonacci_seq.append(next_term)
print("Fibonacci sequence:", fibonacci_seq)

# Loop to iterate over a list and perform operations
numbers = [2, 4, 6, 8, 10]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print("Squared numbers:", squared_numbers)

# Loop to iterate over a string and count the occurrences of a character
word = "banana"
char = "a"
count = 0
for c in word:
    if c == char:
        count += 1
print("Occurrences of", char, "in", word, ":", count)

# Loop to iterate over a dictionary and print key-value pairs
student_grades = {"John": 85, "Emma": 92, "Michael": 78, "Sophia": 90}
print("Student Grades:")
for student, grade in student_grades.items():
    print(student, ":", grade)

# Loop to iterate over a range in reverse order
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# Loop to iterate over multiple lists simultaneously
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
print("Sum of corresponding elements in three lists:")
for n1, n2, n3 in zip(numbers1, numbers2, numbers3):
    print(n1 + n2 + n3)

# Loop to iterate over a list and skip certain elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers skipping multiples of 3:")
for num in numbers:
    if num % 3 == 0:
        continue
    print(num)

# Loop to iterate over a list and break at a certain condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers until reaching 5:")
for num in numbers:
    print(num)
    if num == 5:
        break


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        total = sum(self.grades)
        return total / len(self.grades) if len(self.grades) > 0 else 0

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_average_grade(self):
        total = 0
        num_students = len(self.students)
        for student in self.students:
            total += student.calculate_average()
        return total / num_students if num_students > 0 else 0
    
    def get_maximum_grade(self):
        max_grade = 0
        for student in self.students:
            max_grade = max(max_grade, max(student.grades))
        return max_grade
    
    def get_minimum_grade(self):
        min_grade = 100
        for student in self.students:
            min_grade = min(min_grade, min(student.grades))
        return min_grade
    
    def sort_students_by_average_grade(self):
        sorted_students = sorted(self.students, key=lambda student: student.calculate_average(), reverse=True)
        return sorted_students
    
    def get_students_with_highest_average_grade(self, num_students):
        sorted_students = self.sort_students_by_average_grade()
        return sorted_students[:num_students]
    
    def get_students_with_lowest_average_grade(self, num_students):
        sorted_students = self.sort_students_by_average_grade()
        return sorted_students[-num_students:]

# Create students
student1 = Student("John Doe", 12345)
student2 = Student("Jane Smith", 67890)
student3 = Student("David Johnson", 54321)

# Create a course
course = Course("Mathematics")

# Add students to the course
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# Add grades for each student
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2.add_grade(92)
student2.add_grade(88)
student2.add_grade(95)

student3.add_grade(80)
student3.add_grade(85)
student3.add_grade(90)

# Calculate and display average grade for each student
for student in course.students:
    average_grade = student.calculate_average()
    print(f"Student: {student.name} (ID: {student.id})")
    print(f"Average Grade: {average_grade}\n")

# Calculate and display average grade for the course
average_course_grade = course.get_average_grade()
print(f"Course: {course.name}")
print(f"Average Course Grade: {average_course_grade}")

# Calculate and display maximum grade for the course
maximum_grade = course.get_maximum_grade()
print(f"Maximum Grade in the Course: {maximum_grade}")

# Calculate and display minimum grade for the course
minimum_grade = course.get_minimum_grade()
print(f"Minimum Grade in the Course: {minimum_grade}")

# Sort students by average grade and display
sorted_students = course.sort_students_by_average_grade()
print("Students sorted by Average Grade:")
for student in sorted_students:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")

# Get students with the highest average grade and display
num_students_highest_grade = 2
students_highest_grade = course.get_students_with_highest_average_grade(num_students_highest_grade)
print(f"\nStudents with the Highest Average Grade ({num_students_highest_grade}):")
for student in students_highest_grade:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")

# Get students with the lowest average grade and display
num_students_lowest_grade = 1
students_lowest_grade = course.get_students_with_lowest_average_grade(num_students_lowest_grade)
print(f"\nStudents with the Lowest Average Grade ({num_students_lowest_grade}):")
for student in students_lowest_grade:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")


import random

class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.medals = {"Gold": 0, "Silver": 0, "Bronze": 0}

    def win_medal(self, medal_type):
        self.medals[medal_type] += 1

    def get_total_medals(self):
        return sum(self.medals.values())

class Event:
    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def conduct_event(self):
        # Simulate the event and determine winners
        gold_winner = random.choice(self.participants)
        silver_winner = random.choice([athlete for athlete in self.participants if athlete != gold_winner])
        bronze_winner = random.choice([athlete for athlete in self.participants if athlete != gold_winner and athlete != silver_winner])

        # Award medals to winners
        gold_winner.win_medal("Gold")
        silver_winner.win_medal("Silver")
        bronze_winner.win_medal("Bronze")

    def display_results(self):
        print(f"\n{self.name} Results:")
        print("----------------------")
        for i, athlete in enumerate(self.participants, start=1):
            print(f"{i}. {athlete.name} ({athlete.country}) - Gold: {athlete.medals['Gold']}, Silver: {athlete.medals['Silver']}, Bronze: {athlete.medals['Bronze']}")
        print("----------------------")

class OlympicGames:
    def __init__(self, events, countries):
        self.events = events
        self.countries = countries

    def conduct_olympics(self):
        print("Welcome to the Olympic Games!")
        print("-----------------------------")

        for event in self.events:
            print(f"\n{event.name} is starting...")
            event.conduct_event()
            event.display_results()

        print("\nOlympic Games concluded!")
        print("------------------------")

        overall_medal_table = self.generate_overall_medal_table()
        print("\nOverall Medal Table:")
        print("-------------------")
        for i, country in enumerate(overall_medal_table, start=1):
            total_medals = sum(country.values())
            gold_medals = country["Gold"]
            silver_medals = country["Silver"]
            bronze_medals = country["Bronze"]
            print(f"{i}. {country['Name']} - Gold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals} (Total: {total_medals})")
        print("-------------------")

    def generate_overall_medal_table(self):
        medal_table = {}
        for country in self.countries:
            country_medals = {"Name": country, "Gold": 0, "Silver": 0, "Bronze": 0}
            for event in self.events:
                for athlete in event.participants:
                    if athlete.country == country:
                        country_medals["Gold"] += athlete.medals["Gold"]
                        country_medals["Silver"] += athlete.medals["Silver"]
                        country_medals["Bronze"] += athlete.medals["Bronze"]
            medal_table[country] = country_medals
        sorted_medal_table = sorted(medal_table.items(), key=lambda x: sum(x[1].values()), reverse=True)
        return [medal[1] for medal in sorted_medal_table]

# Define athletes
athlete1 = Athlete("John Doe", "USA")
athlete2 = Athlete("Jane Smith", "USA")
athlete3 = Athlete("David Johnson", "Canada")
athlete4 = Athlete("Emma Wilson", "Canada")
athlete5 = Athlete("Michael Brown", "Great Britain")
athlete6 = Athlete("Sophia Anderson", "Great Britain")

# Define events
event1 = Event("100m Sprint", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])
event2 = Event("Long Jump", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])
event3 = Event("Swimming", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])

# Define Olympic Games
olympics = OlympicGames([event1, event2, event3], ["USA", "Canada", "Great Britain"])

# Conduct and display the results of the Olympic Games
olympics.conduct_olympics()


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
