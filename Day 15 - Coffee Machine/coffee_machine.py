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

def insert_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))


def order_cofee(drink):
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Unable to make drink, insufficient water 💧")
        elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Unable to make drink, insufficient milk 🥛")
        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Unable to make drink, insufficient coffee ☕️")
        else:
            if inserted_money < MENU[drink]["cost"]:
                print(f"Please insert money. Current balance: {inserted_money}, required balance: {MENU[drink]["cost"]}")
                inserted_money()
    else:
        print("Drink is not sold here.")

machine_on = True
inserted_money = 0

# TODO 1. Prompt user by asking 'what would you like?' 
while machine_on:
    user_input = input("What would you like?: ").lower()

    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml 💧")
        print(f"Milk: {resources["milk"]}ml 🥛")
        print(f"Coffee: {resources["coffee"]}g ☕️")
        print(f"Money: ${inserted_money}")
    
    # TODO 4. Check resources are sufficient
    elif user_input == "espresso":

    elif user_input == "latte":

    elif user_input == "cappuccino":


    # TODO 5. Process coins


    # TODO 6. Check transaction successful


    # TODO 7. Make Coffee