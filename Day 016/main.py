from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

while machine_on:
    order = input(f"What would you like? {coffee_menu.get_items()}")

    if order == "off":
        print("Shutting down ...")
        machine_on = False
    elif order == "report":
        coffee_machine.report()
        register.report()
    elif not coffee_menu.find_drink(order) is None:
        # check if order is on the menu
        order = coffee_menu.find_drink(order)
        # setting order to an MenuItem Object
        if coffee_machine.is_resource_sufficient(order):
            # checking for ingredients
            if register.make_payment(order.cost):
                # processing money and creating coffee if successful
                coffee_machine.make_coffee(order)
    else:
        print("Please try again.")
