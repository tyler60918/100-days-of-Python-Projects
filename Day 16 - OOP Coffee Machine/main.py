from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

system_on = True

while system_on:
    user_input = input("What would you like?: ").lower()

    if user_input == "off":
        system_on = False
        continue
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_input)

        if not menu_item:
            continue
        else:
            if coffee_maker.is_resource_sufficient(menu_item):
                paid = money_machine.make_payment(menu_item.cost)
                if paid:
                    coffee_maker.make_coffee(menu_item)

