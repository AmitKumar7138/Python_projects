from data import MENU, resources


def rest(item1, item2):
    return item1 - item2


def take_order(order):
    for ingredient, amount in MENU[order]["ingredients"].items():
        if resources[ingredient] < amount:
            return False
    for ingredient, amount in MENU[order]["ingredients"].items():
        resources[ingredient] -= amount
    return True


def restock(water, milk, coffee):
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee


def take_money(order, residual_change):
    if take_order(order):
        price = MENU[order]["cost"]
        if residual_change >= price:
            return residual_change - price
        else:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = quarters * 0.25 + dimes * \
                0.10 + nickles * 0.05 + pennies * 0.01
            total_money = money_inserted + residual_change
            if total_money >= price:
                return total_money - price
    return False


def response(order):
    return order in ["report", "espresso", "latte", "cappuccino"]


money = 0
order = input(
    "What would you like? (espresso/latte/cappuccino/report): ").lower()

while response(order):
    if order == "report":
        for resource, amount in resources.items():
            print(f"{resource.capitalize()}: {amount}")
        print(f"Money: ${money:.2f}")
    else:
        change = take_money(order, money)
        if change is not False:
            money += MENU[order]["cost"]
            print(f"Here is your {order}. ☕Enjoy!")
            print(f"Here is ${change:.2f} in change.")
        else:
            print("Sorry, we do not have enough resources or insufficient funds.")

    order = input(
        "What would you like? (espresso/latte/cappuccino/report): ").lower()
