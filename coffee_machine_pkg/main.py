from coffee_machine_pkg.coffee_maker import CoffeeMaker
from coffee_machine_pkg.money_machine import MoneyMachine
from coffee_machine_pkg.menu import Menu, MenuItem

over_transaction = False
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while not over_transaction:
    items = menu.get_items()
    answer = input(f"What would you like? ({items})? ").lower()
    if answer == 'report':
        coffee_maker.report()
        money_machine.report()
    elif answer == 'off':
        over_transaction = True
    else:
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough ingredients.")



