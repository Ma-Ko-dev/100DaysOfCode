import random
import hangman_words
import hangman_art

# some initial variables
won = False
lives = 6
guessed = []
display = []

# generate wordlist and get a random word to guess
chosen_word = random.choice(hangman_words.word_list)

# printing the logo at the start
print(hangman_art.logo)

# Testing code. remove before actual playing :D
print(f'Pssst, the solution is {chosen_word}.')
# fill display with _ as replacement for each letter in chosen_word
for _ in range(0, len(chosen_word)):
    display.append("_")

# the game loop
while not won:
    # get userinput and save it
    guess = input("Please enter your best guess: \n").lower()

    if guess in guessed:
        # checking if the user already guessed that letter
        print(f"You already guessed {guess}. Please try again!")
    elif guess in chosen_word:
        print(f"You guessed {guess}. That's in the word!")
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                # replacing the blank with the guessed letter
                display[index] = chosen_word[index]
    else:
        # reducing lives if the guess letter is not in the word
        print(f"You guessed {guess}. That's not in the word, you loose a life!")
        lives -= 1

    guessed.append(guess)
    # printing the art and the formated word
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    if "_" not in display and lives > 0:
        won = True
        print("You won!")
    elif lives == 0:
        won = True
        print("You lost!")

