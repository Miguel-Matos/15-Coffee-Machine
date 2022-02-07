import menu


#print(MENU['espresso']["ingredients"]["water"]) reminder how to access items in a dictionary

#TODO figure out a way to change the keys via a loop to reduce the repetitive code
#TODO redo the coffe_machine if statements so all resources are in stock before it can make the coffee.

def coffee_machine():  
    machine_is_on = True
    while machine_is_on:
        customer_request = input("What would you like? Espresso, Latte, or Cappuccino: ").lower()
        if customer_request == "espresso": #made a separate if statement for espresso as it doesnt have a milk dictionary key.
            print(menu.MENU[customer_request])
            if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] <= 0:
                print(f"Not enough water")
            else:
                menu.resources["water"] -= menu.MENU[customer_request]["ingredients"]["water"]
            if menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] <= 0:
                print(f"Not enough coffee")
            else:
                menu.resources["coffee"] -= menu.MENU[customer_request]["ingredients"]["coffee"]
                money(customer_request)
            print(menu.resources)
            
        if customer_request == "latte" or customer_request == "cappuccino":
            print(menu.MENU[customer_request])
            if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] <= 0:
                print(f"Not enough water")
            else:
                menu.resources["water"] -= menu.MENU[customer_request]["ingredients"]["water"]
            if menu.resources["milk"] - menu.MENU[customer_request]["ingredients"]["milk"] <= 0:
                print(f"Not enough milk")
            else:
                menu.resources["milk"] -= menu.MENU[customer_request]["ingredients"]["milk"]
            if menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] <= 0:
                print(f"Not enough coffee")
            else:
                menu.resources["coffee"] -= menu.MENU[customer_request]["ingredients"]["coffee"]
            print(menu.resources)
        if customer_request == "refill":
            refill()
        elif customer_request == "report":
                print(menu.resources)
        machine_is_on = False
    if customer_request == "off":
        print("Goodbye!")
    elif customer_request != "off":
        coffee_machine()

def refill():
    menu.resources["water"] += 200
    menu.resources["milk"] += 100
    menu.resources["water"] += 50
    print(menu.resources)

def money(customer_order):
    machine_money = 0
    while machine_money < menu.MENU[customer_order]["cost"]:
        insert_coin = input("Please insert a nickle, dime, quarter, or dollar: ").lower()
        if insert_coin == "nickle":
            machine_money += 0.05
        elif insert_coin == "dime":
            machine_money += 0.1
        elif insert_coin == "quarter":
            machine_money += 0.25
        elif insert_coin == "dollar":
            machine_money += 1
        print(machine_money)
    machine_money -= menu.MENU[customer_order]["cost"]
    print(f"Here is your {customer_order} and your change is {machine_money:.2f}.")
    
#customer_request()
coffee_machine()