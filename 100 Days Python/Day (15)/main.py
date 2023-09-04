# Define the MENU dictionary with coffee options and their ingredients/cost
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

# Initialize profit variable to keep track of earnings
profit = 0

# Initialize resources dictionary with available resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Define the function is_resource_sufficient to check if there are enough ingredients
def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be made and False when there are insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            print("Type 'refill' if you wish to top up all the ingredients")
            return False
    return True


# Define the function process_coins to calculate the total money received
def process_coins():
    """Returns the total coins inserted into the coffee machine"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Define the function is_transaction_successful to process payment
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if the money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# Define the function make_coffee to deduct ingredients and serve coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources and serve coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Implement the main program loop
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill":
        # Add an option to refill ingredients
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print("Ingredients have been refilled.")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice. Please select from the menu.")
