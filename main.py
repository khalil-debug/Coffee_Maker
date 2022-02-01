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
    "water": 1000,
    "milk": 400,
    "coffee": 100,
    "money": 0,
}


# TODO: 1. asking the question about what does the user want

def question_coffee():
    response = ""
    verify = False
    while verify == False:
        response = ""
        response = input("What would you like? (espresso/cappuccino/latte)")
        if (response == "latte") or (response == "cappuccino") or (response == "espresso") or (response == "off") or (
                response == "report"):
            verify = True

    print(response)
    if response == "off":
        print("Have a nice day! :)")
        return False
    elif response == "report":
        report()
        question_coffee()
    elif (response != "off") or (response != "report"):
        if check_resources(response):
            quarters = int(input("enter how much quarters: "))
            dimes = int(input("enter how much dimes: "))
            nickles = int(input("enter how much nickles: "))
            pennies = int(input("enter how much pennies: "))
            entered_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
            if money(response, entered_money) == 2:
                resources["money"] += entered_money
                print(f"Here's your {response}. Enjoy!")
                question_coffee()
            elif money(response, entered_money) == 1:
                change = entered_money - MENU[response]["cost"]
                resources["money"] += MENU[response]["cost"]
                print(f"Here's {round(change, 2)}$ in change.")
                print(f"Here's your {response}. Enjoy!")
                question_coffee()
            elif money(response, entered_money) == 0:
                print("That's not enough money, money Refunded!")
                question_coffee()
        else:
            check_resources(response)
            question_coffee()


# TODO: 2. checking if the resources are available or not
def check_resources(for_coffee):
    res=True
    if resources["water"] < MENU[for_coffee]["ingredients"]["water"]:
        print("Sorry there isn't any water left!")
        return False
    else:
        resources["water"] = resources["water"] - MENU[for_coffee]["ingredients"]["water"]

    if resources["coffee"] < MENU[for_coffee]["ingredients"]["coffee"]:
        print("Sorry there isn't any coffee left!")
        return False
    else:
        resources["coffee"] = resources["coffee"] - MENU[for_coffee]["ingredients"]["coffee"]

    if for_coffee != "espresso":
        if resources["milk"] < MENU[for_coffee]["ingredients"]["milk"]:
            print("Sorry there isn't any milk left!")
            return False
        else:
            resources["milk"] = resources["milk"] - MENU[for_coffee]["ingredients"]["milk"]
            return True


# TODO: 3. checking if the money is sufficient
def money(for_coffee, entered_money):
    if MENU[for_coffee]["cost"] > entered_money:
        print("That's not enough money!")
        return 0
    elif MENU[for_coffee]["cost"] < entered_money:
        return 1
    elif MENU[for_coffee]["cost"] == entered_money:
        return 2


# TODO: 4. making a full report about ingredients
def report():
    print(f"There is {resources['water']}ml of water. \n"
          f"{resources['milk']}ml of milk. \n"
          f"{resources['coffee']}g of coffee. \n"
          f"and {resources['money']}$")


# TODO: 5. main application.
question_coffee()
