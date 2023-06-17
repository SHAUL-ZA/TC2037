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
