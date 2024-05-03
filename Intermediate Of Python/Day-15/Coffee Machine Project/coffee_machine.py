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

is_on = True
money = 0


def is_resources_sufficient(order_ingredients):
    """This function checks resources and returns true or false"""
    for i in order_ingredients:
        if order_ingredients[i] <= resources[i]:
            return True
        else:
            print(f"Sorry there is not enough {i}")
            return False


def process_coins():
    """This function accepts coins and returns total money"""
    print("Please insert coins !")
    total = int(input("How many quarters ? ")) * 0.25
    total += int(input("How many dimes ? ")) * 0.1
    total += int(input("How many nickles ? ")) * 0.05
    total += int(input("How many pennies ? ")) * 0.01
    return total


def is_payment_successfull(money_recieved, order_cost):
    """This function takes total money and cost and checks if money is enough or not"""
    if money_recieved >= order_cost:
        change = round(payment - drink['cost'],2)
        print(f"Here is your change : ${change}")
        global money
        money += order_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded !")
        return False


def make_coffee(drink_name, order_ingredients):
    """This function makes coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")


while is_on:
    choice = input("What do you want (espresso/latte/cappuccino) ? ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        drink_ingredients = drink['ingredients']
        if is_resources_sufficient(drink_ingredients):
            payment = process_coins()
            if is_payment_successfull(payment, drink['cost']):
                make_coffee(choice, drink_ingredients)
