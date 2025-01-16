from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_money_machine=MoneyMachine()
my_menu= Menu()
my_coffee_maker=CoffeeMaker()
power_on =True
MENU=my_menu.get_items()
while power_on:
    order= input ("What would you like?(espresso/latte/cappuccino): ").lower()
    
    if order in MENU:
        drink=my_menu.find_drink(order)
        resources_sufficient=my_coffee_maker.is_resource_sufficient(drink)
        paid=my_money_machine.make_payment(drink.cost)
        if resources_sufficient:
            if paid:
                my_coffee_maker.make_coffee(drink)
        else:
            print("You dont have enough resources for this")
    elif order== 'off':
        print("Good Day")
        power_on=False
    elif order =='report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        print("Invalid input")
    