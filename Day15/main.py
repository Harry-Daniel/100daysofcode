MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    },
}

resources= {
    "water":500,
    "milk":450,
    "coffee":100,
    "money": 2.5
}


def customers_order(menu,order,resources):
    beverage=menu[order]["ingredients"]
    insufficient= []
    for key in beverage:
        if beverage[key]>resources[key]:
            insufficient.append(key)
        elif beverage[key]<=resources[key]:
            resources[key]-=beverage[key] 
    
    if not insufficient ==[]:
        return f"The following ingredients are insufficient: {insufficient}"
    return resources


def total_amount_and_change(quarters,dimes,nickles,pennies,order):
    beverage_cost= MENU[order]['cost']
    
    total=0
    total+=0.25*quarters
    total+=0.10*dimes
    total+=0.05*nickles
    total+=0.01*pennies

    if total == beverage_cost:
        return f"Here is your drink. Thank you"
    elif total> beverage_cost:
        return f"Here is your drink.\n Here is your change ${total-beverage_cost}"
    elif total<beverage_cost:
        return f"Your money is not sufficient. Money refunded"
    
    

    
 


power_on=True
while  power_on :
    order= input ("What would you like?(espresso/latte/cappuccino): ").lower()

    if order in MENU:
        resources=customers_order(MENU,order,resources)
        if type(resources) == str:
            print(resources)
        else:
            quarters =int(input("How many quarters"))
            dimes =int(input("How many dimes"))
            nickles =int(input("How many nickles"))
            pennies =int(input("How many pennies"))
            print(total_amount_and_change(quarters,dimes,nickles,pennies,order))
    elif order == 'off':
        print("Good Day")
        power_on=False
    elif order =='report':
        print(f"{resources}\n water and milk measured in ml , coffee in g money in $")
    else:
        print("Invalid input")