from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
Coffe = CoffeeMaker()
pay = MoneyMachine()
inp = input(f"What would you like? {menu.get_items()}: ")
order = menu.find_drink(inp)

while inp != 'off':
    if inp == 'report':
        Coffe.report()
        pay.report()

    else:
        if Coffe.is_resource_sufficient(order) and pay.make_payment(order.cost):
            Coffe.make_coffee(order)

    inp = input(f"What would you like? {menu.get_items()}: ")
    order = menu.find_drink(inp)
