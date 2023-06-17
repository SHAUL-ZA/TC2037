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
