from random import randint
from art import logo

print(logo)

# default variables
win = False
# constants
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty(user_input):
    """Takes a String as Argument and returns the amount of temps as Integer. Also prints a response to the difficulty
    chosen."""
    if user_input == "easy":
        print("You have choose the easy Mode!")
        return EASY_ATTEMPTS
    elif user_input == "hard":
        print("You have choose the easy Mode!")
        return HARD_ATTEMPTS
    else:
        # in case of wrong input, easy is default
        print("You misspelled or didn't enter anything. Game started in easy Mode!")
        return EASY_ATTEMPTS


def check_num(guess, randnum):
    """Takes guess as Integer and randnum as Integer. Prints a statement if the guess is too low/high and returns a
    bool depending on if the user won or not """
    if guess > randnum:
        print("Too high.")
        return False
    elif guess < randnum:
        print("Too low.")
        return False
    else:
        print("Found it!")
        return True


print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty! Type 'easy' or 'hard': ").lower()

attempts = set_difficulty(difficulty)
rand_num = randint(1, 100)
# print(f"DEBUG: {rand_num}")

while attempts > 0:
    # looping until the user runs out of guesses or wins
    print(f"You have {attempts} attempts remaining to guess the number!")
    user_guess = int(input("Make a guess: "))
    win = check_num(user_guess, rand_num)
    attempts -= 1

    if win:
        # if win is True the attempts will be set to 0 so the loop will end
        attempts = 0

print("\n")

if win:
    print("Congratulations! You found the Number and won!")
else:
    print("Too bad! You didn't found the Number! You lost!")
