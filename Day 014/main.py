import art
import random
from game_data import data


def check_duplicate(comp_1, comp_2):
    while comp_1 == comp_2:
        comp_2 = random.choice(data)
    return comp_2


def get_user_input():
    user = input("Who has more followers? Type 'A' or 'B': ").lower()
    # maybe check the input here? Otherwise, this function is of course useless atm
    return user


def check_answer(guess, comp_1, comp_2):
    # comp_1 == a / comp_2 == b
    if comp_1 > comp_2:
        return guess == "a"
    else:
        return guess == "b"


def run_game():
    comp_1 = random.choice(data)
    # setting comp_2 to a random data and checking if it's the same as comp_1
    comp_2 = check_duplicate(comp_1, random.choice(data))
    user_score = 0

    print(f"Compare A: {comp_1['name']}, a {comp_1['description']}, from {comp_1['country']}")
    print(art.vs)
    print(f"Against B: {comp_2['name']}, a {comp_2['description']}, from {comp_2['country']}")

    user_input = get_user_input()

    while check_answer(user_input, comp_1["follower_count"], comp_2["follower_count"]):
        user_score += 1
        print(f"You are right! Current Score {user_score}.")
        comp_1 = comp_2
        comp_2 = check_duplicate(comp_1, random.choice(data))

        print(f"Compare A: {comp_1['name']}, a {comp_1['description']}, from {comp_1['country']}")
        print(art.vs)
        print(f"Against B: {comp_2['name']}, a {comp_2['description']}, from {comp_2['country']}")

        user_input = get_user_input()

    # Game Over
    print(f"Sorry, that's wrong. Final Score {user_score}")
    return


print(art.logo)
run_game()
