# This is a virtual coffee maker written in Python.
# Using OOP, there are 3 classes that are used to simulate
# a coffee machine.
# The user has 3 valid commands that they can use:
#    report - show a report of the resources
#    latte/espresso/cappuccino - to place an order for a coffee
#    off - to turn the coffee maker off and exit the program
# When placing an order, the user will be prompted for different
# coins to pay for the order.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

# coffee_maker.report()
# money_machine.report()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
