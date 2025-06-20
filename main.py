import menu as menu_module
import resources as resources_module

def report():
    for resource in resources_module.resources:
        print(f"{resource.title()}: {resources_module.resources[resource]}")

def check_resource(choice):
    ingredients = menu_module.menu[choice]["ingredients"]
    insufficient_ingredients = []
    for ingredient_name in ingredients:
        resource_left = resources_module.resources[ingredient_name] - ingredients[ingredient_name]
        if resource_left < 0:
            insufficient_ingredients.append(ingredient_name)
    if len(insufficient_ingredients) > 0:
        msg = ", ".join(insufficient_ingredients)
        print(f"Sorry. There is not enough {msg}.")
        return False
    return True

def print_price(choice):
    print(f"Price for a cup of {choice}: ${menu_module.menu[choice]['cost']}")

def cashier(choice):
    total_payment = 0.00
    cost = menu_module.menu[choice]["cost"]
    while total_payment < cost:
        try:
            user_input = input("Please insert coins (or 'cancel' to return to menu): $")
            if user_input == "cancel":
                print(f"Payment cancelled. Here is your change: $ {total_payment}")
                return False
            inserted_amount = round(float(user_input),2)
            print(inserted_amount)
            if inserted_amount <= 0:
                print("Please insert a positive amount.")
                continue
            total_payment += inserted_amount
            print(f"Current payment: ${total_payment}")
        except ValueError:
            print("Invalid input. Please enter a numerical amount: $")
    change = total_payment - cost
    resources_module.resources["money"] += cost
    if change > 0:
        print(f"Here is ${change} in change.")
    return True

def produce_coffee(choice):
    ingredients = menu_module.menu[choice]["ingredients"]
    for ingredient_name in ingredients:
        resources_module.resources[ingredient_name] -= ingredients[ingredient_name]
    print(f"Here is your {choice}. Enjoy!")

def turn_off_msg():
    print(f"Good Bye! Have a nice day!")

def coffee_machine():
    choices_list = ["espresso", "latte", "cappuccino", "report", "turn off"]
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/report/turn off): ").lower()
        while choice not in choices_list:
            choice = input("Invalid option.\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            report()
        elif choice == "turn off":
            turn_off_msg()
            break
        else:
            can_produce = check_resource(choice)
            if can_produce:
                print_price(choice)
                payment_successful = cashier(choice)
                if payment_successful:
                    produce_coffee(choice)

coffee_machine()
