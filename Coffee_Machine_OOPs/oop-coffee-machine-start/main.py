from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
Coffe = CoffeeMaker()
pay = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    inp = input(f"What would you like? {options}: ")

    if inp == "off":
        is_on = False

    elif inp == "report":
        Coffe.report()
        pay.report()

    else:
        order = menu.find_drink(inp)

        if Coffe.is_resource_sufficient(order) and pay.make_payment(order.cost):
            Coffe.make_coffee(order)
