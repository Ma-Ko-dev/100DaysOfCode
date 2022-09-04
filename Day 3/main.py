# Just a short Adventure with some control flow as learned in today's lecture
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("")
print("You are in the big City. You are on your way home and see a little cat on the side of the road. What are you "
      "doing? Do you go to the 'cat' or do you go 'past' the cat?")
quest = input("Please type 'cat' or 'past' now!\n").lower()
if quest == "cat":
    print("Good! You approach the cat carefully and crouch down to pet it. The cat is very friendly and let you pet "
          "it. You can feel that she is very skinny. What do you do?")
    quest = input("Do you try to 'take' the cat or do you leave it alone and go 'home'?\n").lower()
    if quest == "take":
        print("Good! The cat seems to understand what your plan is and follows you on its own. You arrive at home and "
              "you find something to eat for her.\n")
        quest = "success"
    else:
        quest = "failed"
        print("You left the cat starving. A sad end for an animal.\n")
else:
    quest = "failed"
    print("You left the cat alone.\n")

if quest == "success":
    # cat ascii
    print('''
    ******************************************************
                                _.---.
                      |\---/|  / ) ca|
          ------------;     |-/ /|foo|---
                      )     (' / `---'
          ===========(       ,'==========
          ||   _     |      |
          || o/ )    |      | o
          || ( (    /       ;
          ||  \ `._/       /
          ||   `._        /|
          ||      |\    _/||
        __||_____.' )  |__||____________
         ________\  |  |_________________
                  \ \  `-.
                   `-`---'  hjw
    *******************************************************
   ''')
    print("Congratulations! You helped an Animal in need and probably found a friend for life! The treasure you found " 
          " today is a companion for life!")
else:
    print("Unfortunately for you, you didn't found any treasure today.")
