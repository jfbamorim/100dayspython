################################################################
# Day 15 - Intermediate - Coffee Machine Project
################################################################
from dayfifteen.coffee_machine_data import MENU, resources

def print_all_options(money):
    """ Print in output all the options for coffee in the machine """
    for resource in resources:
        print(f"{resource.capitalize()}: {resources[resource]}ml")
    print(f"Money: ${money}")


def prepare(option):
    """ Verify if there are all the resources needed to prepare the option choosed by user """
    ingredients = MENU[option]
    water_needed = ingredients["ingredients"]["water"]
    coffee_needed = ingredients["ingredients"]["coffee"]
    if option != "espresso":
        milk_needed = ingredients["ingredients"]["milk"]
    else:
        milk_needed = 0
    if water_needed > resources["water"]:
        print("Sorry there is not enough water.")
    elif coffee_needed > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    elif milk_needed > resources["milk"]:
        print("Sorry there is not enough milk.")
    else:
        resources["water"] = resources["water"] - water_needed
        resources["coffee"] = resources["coffee"] - coffee_needed
        resources["milk"] = resources["milk"] - milk_needed

        print(f"Here is your {option} ☕️. Enjoy!")


def process_request(option_ch):
    """ Process the type of coffee that the user requested """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_received = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    global options, total_money
    if option_ch in options and total_received >= MENU[option_ch]["cost"]:
        return_money = round(total_received - MENU[option_ch]["cost"], 2)
        if return_money > 0.00:
            print(f"Here is ${return_money} dollars in change")
        total_money += options[option_ch]
        prepare(option_ch)
    else:
        print("Sorry that's not enough money. Money refunded.")


options = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappuccino": 3.00
}
total_money = 0
over_transaction = False
while not over_transaction:
    answer = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if answer == 'report':
        print_all_options(total_money)
    elif answer == 'off':
        over_transaction = True
    else:
        process_request(answer)
