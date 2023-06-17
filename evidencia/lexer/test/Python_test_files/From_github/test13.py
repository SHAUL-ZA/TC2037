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
