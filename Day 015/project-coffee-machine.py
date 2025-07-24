# Coffee Machine Program
from art import logo
print(logo)
# MENU dictionary containing drink options, ingredients required, and cost
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

# Initial available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to process coins and return whether payment is successful
# Q: Process coins and check if transaction is successful?
def money(quarters, dimes, nickles, pennies, drink):
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total >= MENU[drink]["cost"]:
        change = round(total - MENU[drink]["cost"], 2)
        print(f"Here is your coffee, and here is your ${change} change.")
        return True
    else:
        print(f"Sorry, that's insufficient. You gave ${total}, but {drink} costs ${MENU[drink]['cost']}.")
        return False

# Function to check if machine has enough resources
# Q: Check if resources are sufficient?
def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

# Function to make coffee and deduct used ingredients
# Q: Make coffee and deduct ingredients?
def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕. Enjoy!")

# Q: Start main coffee machine loop to take orders?
is_order = True
while is_order:
    # Q: Ask user for their choice (espresso/latte/cappuccino)?
    user_order = input("What would you like? espresso/latte/cappuccino/report/off: ").lower()

    # Q: Check if user wants to turn off the machine?
    if user_order == "off":
        is_order = False

    # Q: Print current resources if user types "report"?
    elif user_order == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")

    # Q: Proceed only if user input matches a valid drink?
    elif user_order in MENU:
        # Q: Check if there are enough resources to make selected drink?
        if check_resources(user_order):
            # Q: Ask user to input coins?
            user_money_quarters = float(input("Enter quarters: "))
            user_money_dimes = float(input("Enter dimes: "))
            user_money_nickles = float(input("Enter nickles: "))
            user_money_pennies = float(input("Enter pennies: "))

            # Q: If payment is sufficient, make the coffee?
            if money(user_money_quarters, user_money_dimes, user_money_nickles, user_money_pennies, user_order):
                make_coffee(user_order)

    # Q: Handle invalid input?
    else:
        print("Invalid input. Please choose again.")
