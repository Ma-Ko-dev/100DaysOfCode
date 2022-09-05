import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# storing the art in a list and getting the player input. Also determine the PCs choice randomly.
art = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice = random.randint(0, 2)

# check player input is in range
if player_choice >= 3 or player_choice < 0:
    print("Please only use 0, 1 and 2 as input!")
else:
    # display what everyone picked
    print("The Player picked:")
    print(f"{art[player_choice]}\n")
    print("The Computer chose:")
    print(f"{art[pc_choice]}\n")

    # check who won
    if player_choice == 0 and pc_choice == 2:
        print("You won!")
    elif player_choice == 1 and pc_choice == 0:
        print("You won!")
    elif player_choice == 2 and pc_choice == 1:
        print("You won!")
    elif player_choice == pc_choice:
        print("It's a draw!")
    else:
        print("You loose!")
