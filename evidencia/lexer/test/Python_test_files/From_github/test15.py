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
