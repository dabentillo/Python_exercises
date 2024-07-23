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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print("remaining resources:")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${float(profit)}")


def machine_off():
    print("machine is now OFF.")


def resource_sufficient(choice):
    resource_ok = False

    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("sorry there is not enough water.")
    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("sorry there is not enough coffee.")
    else:
        resource_ok = True

    if choice != "espresso":
        if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print("sorry there is not enough milk.")
        else:
            resource_ok = True

    return resource_ok


# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def process_coins():
    total_payment = int(input("How many quarters?: ")) * 0.25
    total_payment += int(input("How many dimes?: ")) * 0.10
    total_payment += int(input("How many nickels?: ")) * 0.05
    total_payment += int(input("How many pennies?: ")) * 0.01

    return round(total_payment,2)


def transaction_successful(payment, choice):
    cost_of_order = MENU[choice]["cost"]

    if payment >= cost_of_order:
        global profit
        profit += cost_of_order
        change = round((payment - cost_of_order),2)
        print(f"Here is ${float(round(change,2))} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice):
    if choice == "espresso":
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]

    print(f"Here is your {user_choice}! ☕ Enjoy!")


machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) : ")
    if user_choice == "report":
        print_report()
    elif user_choice == "off":
        machine_off()
        machine_on = False
    else:
        if user_choice not in MENU:
            print("Not in options. Please try again.")
        else:
            if resource_sufficient(user_choice):
                user_payment = process_coins()
                if transaction_successful(user_payment, user_choice):
                    make_coffee(user_choice)
