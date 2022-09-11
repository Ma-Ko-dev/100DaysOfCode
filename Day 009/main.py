import art


def clear_screen():
    # since i cant use a clear command in PyCharm i improvised this hacky solution
    print("\n" * 80)


def get_highest_bid():
    # looping through all bidders and prints who won
    highest_bid = 0
    highest_bid_name = ""
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
            highest_bid_name = key
    print(f"The highest bidder is {highest_bid_name.capitalize()} with ${highest_bid}")


# show logo at first start
print(art.logo)

# initial variables
bidders = {}
get_bids = True

# getting bids
while get_bids:
    # saving bidder and bid
    bid_name = input("Please enter your Name:\n")
    bid_amount = int(input("Please enter your bid:\n"))

    # adding new key:value pair do dic
    bidders[bid_name] = bid_amount

    # finding out if we have to get more bids or if we are done
    start_over = input("Are there any other people who wants to bid? Please Type 'Yes' or 'No':\n").lower()

    if start_over == "no":
        # exiting the loop and printing the highest bid
        get_bids = False
        get_highest_bid()
    else:
        clear_screen()
