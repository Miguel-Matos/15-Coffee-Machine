import menu

def customer_request():
    return input("What would you like? Espresso, Latte, or Cappuccino: ").lower()


#print(MENU['espresso']["ingredients"]["water"]) reminder how to access items in a dictionary

#TODO figure out a way to change the keys via a loop to reduce the repetitive code

def coffee_machine(customer_order):  
    machine_is_on = True
    while machine_is_on:
        if customer_order == "espresso": #made a separate if statement for espresso as it doesnt have a milk dictionary key.
            print(menu.MENU[customer_order])
            if menu.resources["water"] - menu.MENU[customer_order]["ingredients"]["water"] <= 0:
                print(f"Not enough water")
            else:
                menu.resources["water"] -= menu.MENU[customer_order]["ingredients"]["water"]
            if menu.resources["coffee"] - menu.MENU[customer_order]["ingredients"]["coffee"] <= 0:
                print(f"Not enough coffee")
            else:
                menu.resources["coffee"] -= menu.MENU[customer_order]["ingredients"]["coffee"]
                money()
            print(menu.resources)
            
        if customer_order == "latte" or customer_order == "cappuccino":
            print(menu.MENU[customer_order])
            if menu.resources["water"] - menu.MENU[customer_order]["ingredients"]["water"] <= 0:
                print(f"Not enough water")
            else:
                menu.resources["water"] -= menu.MENU[customer_order]["ingredients"]["water"]
            if menu.resources["milk"] - menu.MENU[customer_order]["ingredients"]["milk"] <= 0:
                print(f"Not enough milk")
            else:
                menu.resources["milk"] -= menu.MENU[customer_order]["ingredients"]["milk"]
            if menu.resources["coffee"] - menu.MENU[customer_order]["ingredients"]["coffee"] <= 0:
                print(f"Not enough coffee")
            else:
                menu.resources["coffee"] -= menu.MENU[customer_order]["ingredients"]["coffee"]
            print(menu.resources)
        if customer_order == "refill":
            refill()
        elif customer_order == "report":
                print(menu.resources)
        machine_is_on = False
    if customer_order == "off":
        print("Goodbye!")
    elif customer_order != "off":
        coffee_machine(customer_request())

def refill():
    menu.resources["water"] += 200
    menu.resources["milk"] += 100
    menu.resources["water"] += 50
    print(menu.resources)

def money():
    machine_money = 0
    while machine_money < menu.MENU["espresso"]["cost"]:
        machine_money += .5
        print(machine_money)
    
#customer_request()
coffee_machine(customer_request())