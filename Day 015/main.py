MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.50,
}

machine_running = True


def show_resources():
    """Prints the current contents of the Coffee Machine. Returns nothing."""
    print("The contents of the Coffee Machine are as follows:")
    print(f"Water:\t{resources['water']}ml")
    print(f"Milk:\t{resources['milk']}ml")
    print(f"Coffee:\t{resources['coffee']}g")
    print(f"Money:\t${resources['money']:.2f}")
    pass


def check_resources(drink):
    """Checks if the Machine has enough resources to make the drink it got as an argument. Returns True/False"""
    d_water = MENU[drink]["ingredients"]["water"]
    d_milk = MENU[drink]["ingredients"]["milk"]
    d_coffee = MENU[drink]["ingredients"]["coffee"]

    m_water = resources["water"]
    m_milk = resources["milk"]
    m_coffee = resources["coffee"]

    if not m_water >= d_water:
        print("Sorry there is not enough water.")
        return False
    elif not m_milk >= d_milk:
        print("Sorry there is not enough milk.")
        return False
    elif not m_coffee >= d_coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def sum_coins(quarters, dimes, nickles, pennies):
    """Adds up all coins and returns them. Takes 4 Arguments: quarters, dimes, nickles, pennies"""
    t_quarters = quarters * 0.25
    t_dimes = dimes * 0.10
    t_nickles = nickles * 0.05
    t_pennies = pennies * 0.01
    return t_quarters + t_dimes + t_nickles + t_pennies


def check_money(money, drink):
    """Checks if the money the user gave is enough to buy the drink. Takes 2 arguments: money and drink. Returns
    True/False """
    drink_price = MENU[drink]["cost"]

    if money >= drink_price:
        # user has enough money
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_money(money, drink):
    """The function processes the money it got as an argument. It takes two arguments: money and drink. Returns
    nothing"""
    drink_price = MENU[drink]["cost"]
    money -= drink_price

    if money > 0:
        # giving out change if there is any
        print(f"Here is ${money:.2f} dollars in change.")

    resources["money"] += drink_price
    pass


def make_coffee(drink):
    """Takes drink as argument and reduces the ingredients from the Coffee Machine. Returns nothing"""
    i_water = MENU[drink]["ingredients"]["water"]
    i_milk = MENU[drink]["ingredients"]["milk"]
    i_coffee = MENU[drink]["ingredients"]["coffee"]

    resources["water"] -= i_water
    resources["milk"] -= i_milk
    resources["coffee"] -= i_coffee

    print(f"Here is your {drink.capitalize()}. Enjoy! ☕")
    pass


while machine_running:
    # taking the order from the user
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        # exiting the program/shutting down the machine
        print("Turning off the Machine...")
        machine_running = False
    elif order == "report":
        # shoring the report
        show_resources()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        # checking if the user gave a correct input
        if check_resources(order):
            # checking if there are enough resources
            print("Please insert your Coins!")
            money_q = int(input("Please insert your Quarters: "))
            money_d = int(input("Please insert your Dimes: "))
            money_n = int(input("Please insert your Nickles: "))
            money_p = int(input("Please insert your Pennies: "))
            if check_money(sum_coins(money_q, money_d, money_n, money_p), order):
                # checking if there is enough money for the drink
                process_money(sum_coins(money_q, money_d, money_n, money_p), order)
                make_coffee(order)
    else:
        # no recognized command
        print("Please try again with a correct Order or Command.")
