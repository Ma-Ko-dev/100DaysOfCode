import random
from art import logo

print(logo)

# Initial variables
play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_cards():
    """This Function returns a list of 2 integers. Used to draw the first 2 cards of a Game"""
    return [random.choice(cards), random.choice(cards)]


def draw_card(cards_onhand):
    """Takes a list of Integers and returns the list with on additional Integer"""
    cards_onhand.append(random.choice(cards))
    return cards_onhand


def set_points(cards_onhand):
    """ Takes a list of Integers and checks if it has a 11 in it. If theres a 11 it also checks if the total sum
        would be over 21 and replaces the 11 with an 1 if necessary. Returns the sum of all integers of the list."""
    if 11 in cards_onhand:
        if sum(cards_onhand) > 21:
            cards_onhand[cards_onhand.index(11)] = 1
            return sum(cards_onhand)
        else:
            return sum(cards_onhand)
    else:
        return sum(cards_onhand)


# actual game loop
while play_game:
    # setting or resetting variables used in the gameloop
    player_cards = []
    dealer_cards = []
    player_total = 0
    dealer_total = 0
    draw_more = True
    dealer_more = True

    play_input = input("Do you want to play a game of Black Jack? Type 'y' for Yes and 'n' for No: ")
    print("\n")

    # checking if the user wants to play black jack
    if play_input == "y":
        # drawing and printing the first 2 cards for the player
        print("Your Cards are:")
        player_cards = draw_cards()
        player_total = set_points(player_cards)
        print(f"{player_cards}\n")

        # drawing the first 2 cards for the dealer but only show the last
        print("Dealer Cards:")
        dealer_cards = draw_cards()
        dealer_total = set_points(dealer_cards)
        print(f"[X {dealer_cards[-1]}]")

        # if the player has a natural 21, we skip the draw or stand phase completely
        if player_total == 21:
            print("You got 21! Congratulations!")
        else:
            while draw_more:
                # draw a card as long as the player wants or not goes over 21
                if player_total < 21:
                    draw_more = input("Please type 'd' to draw another card or 's' to stand: ")
                    if draw_more == "d":
                        # draw a card
                        print("Your Cards:")
                        player_cards = draw_card(player_cards)
                        player_total = set_points(player_cards)
                        print(player_cards)
                    else:
                        # no more card
                        draw_more = False
                elif player_total == 21:
                    # the player got to 21 after drawing card/s
                    print("You got 21! Congratulations!")
                    draw_more = False
                else:
                    # player is over 21, meaning he busted
                    print("Busted!\n")
                    draw_more = False

        # takes a new card only if the player didn't bust
        if player_total > 21:
            print("Player busted! Dealer doesnt need any more Cards!")
        else:
            while dealer_more:
                if dealer_total == 21:
                    # if the dealer has a natural 21, he dont need more cards
                    print("Dealer has 21!\n")
                    dealer_more = False
                elif dealer_total < 17:
                    # according to the rules, the dealer has to take a card if he is under 17
                    dealer_cards = draw_card(dealer_cards)
                    dealer_total = set_points(dealer_cards)
                else:
                    # the dealer won't go over 17. he will also show his complete hand now
                    print("Dealers final Cards are:")
                    print(f"{dealer_cards}\n")
                    dealer_total = set_points(dealer_cards)
                    dealer_more = False

        print("The final result is:")
        print(f"The Players Cards are: {player_cards}")
        print(f"The Dealers Cards are: {dealer_cards}\n")
        # now we check who won.
        if player_total > 21:
            print("The Dealer won!")
        elif dealer_total > 21:
            print("The Player won!")
        elif player_total > dealer_total:
            print("The Player won!")
        elif player_total == dealer_total:
            print("Its a draw")
        else:
            print("The Dealer won!")

    # User don't want to play black jack
    else:
        print("Have a nice day!")
        # setting the gameloop flag to False
        play_game = False
