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
