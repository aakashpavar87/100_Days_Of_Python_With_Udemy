MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def print_report():
    return f"Water : {resources['water']}ml \nMilk : {resources['milk']}ml \nCoffee : {resources['coffee']}g \nMoney : ${money}"


def process_coins():
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total


quarters = 0
dimes = 0
nickels = 0
pennies = 0


def take_coins():
    global quarters, dimes, nickels, pennies
    quarters = int(input("how many quarters? : "))
    dimes = int(input("how many dimes? : "))
    nickels = int(input("how many nickels? : "))
    pennies = int(input("how many pennies? : "))


def check_money_suff(coffee_type):
    if MENU[coffee_type]["cost"] < process_coins():
        change = process_coins() - MENU[coffee_type]["cost"]
        global money
        money += MENU[coffee_type]["cost"]
        global resources
        if coffee_type == 'espresso':
            resources["water"] -= MENU[coffee_type]['ingredients']["water"]
            resources["coffee"] -= MENU[coffee_type]['ingredients']["coffee"]
        else:
            resources["coffee"] -= MENU[coffee_type]['ingredients']["coffee"]
            resources["water"] -= MENU[coffee_type]['ingredients']["water"]
            resources["milk"] -= MENU[coffee_type]['ingredients']["milk"]
        print(f"Here is your change ${change}")
        print(f"Enjoy your {coffee_type} ☕.")
    else:
        print(
            f"Sorry money is not sufficient Take your money {process_coins()} as refund."
        )

while True:
    # TODO 1. Prompt User By Asking What would you like
    choice = input("What would you like ? (espresso/latte/cappuccino) Type (report) for checking report  Type (off) for Turn Off Coffee Machine : ")
    if choice == "off":
        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        break
    elif choice == "report":
        # TODO 3. Print report.
        print(print_report())
        continue
    else:
        if choice == "espresso":
            # TODO 4. Check resources sufficient?
            water_req = MENU[choice]["ingredients"]["water"]
            coffee_req = MENU[choice]["ingredients"]["coffee"]
            if resources["water"] < water_req:
                print("Sorry there is not enough water.")
            else:
                take_coins()
                check_money_suff(choice)
        else:
            water_req = MENU[choice]["ingredients"]["water"]
            milk_req = MENU[choice]["ingredients"]["milk"]
            coffee_req = MENU[choice]["ingredients"]["coffee"]

            if (
                resources["water"] < water_req
                or resources["coffee"] < coffee_req
                or resources["milk"] < milk_req
            ):
                print("Sorry there is not enough resources.")
            else:
                take_coins()
                check_money_suff(choice)
