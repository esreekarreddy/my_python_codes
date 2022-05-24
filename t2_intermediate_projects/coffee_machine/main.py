MENU = {
    "espresso": {
        "ingredients": {
            "water": 150,
            "milk": 150,
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

resources = {"water": 1000, "milk": 600, "coffee": 100, "money": 0}


def user_choice(choice):
    check_resources(MENU[choice]["ingredients"])
    quarters = int(input("Enter no of quarters: "))
    dimes = int(input("Enter no of dimes: "))
    nickles = int(input("Enter no of nickles: "))
    pennies = int(input("Enter no of pennies: "))
    cost = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    transaction(cost, choice)
    pick()


def transaction(cost, choice):
    if cost < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return
    if cost > MENU[choice]['cost']:
        print(f"Here's your change: {round(cost - MENU[choice]['cost'], 2)} ")
    print(f"Here is your {choice}. Enjoy!")
    update_resources(choice)


def update_resources(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    resources["money"] += MENU[choice]['cost']


def check_resources(choice_ingredients):
    for item in choice_ingredients:
        if choice_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            pick()


def pick():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice != "off":
        if choice == "report":
            print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}gm\nMoney: ${resources["money"]}')
            pick()
        else:
            user_choice(choice)
    print("Thank you...")
    exit()


pick()