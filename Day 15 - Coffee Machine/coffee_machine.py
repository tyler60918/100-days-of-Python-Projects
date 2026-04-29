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

machine_on = True
inserted_money = 0

def insert_money():
    global inserted_money
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    inserted_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def order_coffee(drink):
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        global inserted_money
        if resources["water"] < MENU[drink]["ingredients"].get("water", 0):
            print("Unable to make drink, insufficient water 💧")
        elif resources["milk"] < MENU[drink]["ingredients"].get("milk", 0):
            print("Unable to make drink, insufficient milk 🥛")
        elif resources["coffee"] < MENU[drink]["ingredients"].get("coffee", 0):
            print("Unable to make drink, insufficient coffee ☕️")
        else:
            if inserted_money < MENU[drink]["cost"]:
                print(f"Please insert money. Current balance: ${inserted_money}, required balance: ${MENU[drink]["cost"]}")
                insert_money()
                if inserted_money < MENU[drink]["cost"]:
                    return False
                else:
                    resources["water"] -= MENU[drink]["ingredients"].get("water", 0)
                    resources["milk"] -= MENU[drink]["ingredients"].get("milk", 0)
                    resources["coffee"] -= MENU[drink]["ingredients"].get("coffee", 0)
                    inserted_money -= MENU[drink]["cost"]
                    return True

    else:
        print("Drink is not sold here.")

while machine_on:
    order_success = False
    user_input = input("What would you like?: ").lower()

    if user_input == "off":
        machine_on = False
        continue
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml 💧")
        print(f"Milk: {resources["milk"]}ml 🥛")
        print(f"Coffee: {resources["coffee"]}g ☕️")
        print(f"Money: ${inserted_money}")
    elif user_input == "espresso":
        order_success = order_coffee("espresso")
    elif user_input == "latte":
        order_success = order_coffee("latte")
    elif user_input == "cappuccino":
        order_success = order_coffee("cappuccino")

    if order_success:
        print(f"{user_input} purchased! ${round(inserted_money, 2)} refunded.")
    else:
        print("Insufficient funds.")