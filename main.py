import menu


#print(MENU['espresso']["ingredients"]["water"]) reminder how to access items in a dictionary

#TODO figure out a way to change the keys via a loop to reduce the repetitive code
#TODO redo the coffe_machine if statements so all resources are in stock before it can make the coffee.

def coffee_machine():  
    machine_is_on = True
    while machine_is_on:
        customer_request = input("What would you like? Espresso, Latte, or Cappuccino: ").lower()
        if customer_request == "espresso": #made a separate if statement for espresso as it doesnt have a milk dictionary key.
            if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] > 0 and menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] > 0:
                menu.resources["water"] -= menu.MENU[customer_request]["ingredients"]["water"]
                menu.resources["coffee"] -= menu.MENU[customer_request]["ingredients"]["coffee"]
                money(customer_request)
                menu.machine_balance += menu.MENU[customer_request]["cost"]
                print(f"Balance is {menu.machine_balance}")
            elif menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0 or menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0:
                if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0 and menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0:
                    print(f"Not enough water")
                    print(f"Not enough coffee")
                elif menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0:
                    print(f"Not enough water")
                elif menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0:
                    print(f"Not enough coffee")
            # print(menu.resources)
            
        if customer_request == "latte" or customer_request == "cappuccino":
            # print(menu.MENU[customer_request])
            if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] > 0 and menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] > 0 and menu.resources["milk"] - menu.MENU[customer_request]["ingredients"]["milk"] > 0:
                menu.resources["water"] -= menu.MENU[customer_request]["ingredients"]["water"]
                menu.resources["coffee"] -= menu.MENU[customer_request]["ingredients"]["coffee"]
                menu.resources["milk"] -= menu.MENU[customer_request]["ingredients"]["milk"]
                money(customer_request)
                menu.machine_balance += menu.MENU[customer_request]["cost"]
            elif menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0 or menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0 or menu.resources["milk"] - menu.MENU[customer_request]["ingredients"]["milk"] < 0:
                if menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0 and menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0 and menu.resources["milk"] - menu.MENU[customer_request]["ingredients"]["milk"] < 0:
                    print(f"Not enough water")
                    print(f"Not enough coffee")
                    print(f"Not enough milk")
                elif menu.resources["water"] - menu.MENU[customer_request]["ingredients"]["water"] < 0:
                    print(f"Not enough water")
                elif menu.resources["coffee"] - menu.MENU[customer_request]["ingredients"]["coffee"] < 0:
                    print(f"Not enough coffee")
                elif menu.resources["milk"] - menu.MENU[customer_request]["ingredients"]["milk"] < 0:
                    print(f"Not enough milk")
        if customer_request == "refill":
            refill()
        elif customer_request == "report":
                print(f"Water: {menu.resources['water']}ml \nMilk: {menu.resources['milk']}ml \nCoffee: {menu.resources['coffee']}g \nMachine Balance: ${menu.machine_balance:.2f}")
        machine_is_on = False
    if customer_request == "off":
        print("Goodbye!")
    elif customer_request != "off":
        coffee_machine()

def refill():
    menu.resources["water"] += 200
    menu.resources["milk"] += 100
    menu.resources["coffee"] += 50
    print(f"Water: {menu.resources['water']}ml \nMilk: {menu.resources['milk']}ml \nCoffee: {menu.resources['coffee']}g")

def money(customer_order):
    machine_money = 0
    print(f"You have chosen {customer_order}. The total is ${menu.MENU[customer_order]['cost']:.2f}.")
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
        if machine_money < menu.MENU[customer_order]["cost"]:
            print(f"You have inserted ${machine_money:.2f}. The total needed is ${menu.MENU[customer_order]['cost']:.2f}")
    machine_money -= menu.MENU[customer_order]["cost"]
    print(f"Here is your {customer_order} and your change is ${machine_money:.2f}.")

#customer_request()
coffee_machine()