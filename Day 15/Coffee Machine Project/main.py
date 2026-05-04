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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

"""
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer
"""
while resources["water"] > 0 and resources["milk"] > 0 and resources["coffee"] > 0:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "espresso":
        choice = MENU["espresso"]
        resources["water"] -= choice["ingredients"]["water"]
        resources["coffee"] -= choice["ingredients"]["coffee"]
        print(f"{resources['water']} water, {resources['coffee']} coffee")
    elif order == "latte":
        choice = MENU["latte"]
    elif order == "cappuccino":
        choice = MENU["cappuccino"]
    else:
        print("Invalid choice.")
        exit()

