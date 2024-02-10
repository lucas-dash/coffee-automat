from storage import menu
from storage import resources

# FUNCTION

# report ingredients

rest_of_ingredients = resources

def calculate_ingredients(drink_name):
    rest_of_ingredients["water"] = rest_of_ingredients["water"] - menu[drink_name]["ingredients"]["water"]
    rest_of_ingredients["milk"] = rest_of_ingredients["milk"] - menu[drink_name]["ingredients"]["milk"]
    rest_of_ingredients["coffee"] = rest_of_ingredients["coffee"] - menu[drink_name]["ingredients"]["coffee"]


def report(password, data):
    admin_password = 1234

    if password == admin_password:
        return f"Water: {data['water']}, Milk: {data["milk"]}, Coffee: {data["coffee"]}"
    else: 
        print("Wrong password.")

def out_of_ingredients(water, milk, coffee):
    if rest_of_ingredients["water"] <= 0:
        print("Out of water. Call a technician.")
        return False
    elif rest_of_ingredients["milk"] <= 0:
        print("Out of milk. Call a technician.")
        return False
    elif rest_of_ingredients["coffee"] <= 0:
        print("Out of coffee. Call a technician.")
        return False
    else:
        return True

# coins handle

def coins(drink):
    sum = int(input(f"Price is CZK {menu[drink]["price"]}. Please insert coins.\n"))
    return sum

def returnCoins(user_coins, drink):
    drink_price = menu[drink]["price"]
    insert_coins = user_coins

    total = insert_coins - drink_price

    if insert_coins >= drink_price:
        makeCoffe()
        if total > 0:
            print(f"Your budget is CZK {sum}")
            print(f"I'm giving you CZK {total} back.")

    elif insert_coins < drink_price:
        coins_left = drink_price - insert_coins

        while insert_coins < drink_price:
            print(f"Your budget is CZK {sum}")
            coins = int(input(f"Add more coins! {coins_left}left!\n"))
            insert_coins += coins

            if insert_coins >= drink_price:
                if insert_coins > drink_price:
                    print(f"I'm giving you CZK {insert_coins - drink_price} back.")
                    makeCoffe()
                else:
                    makeCoffe()


def makeCoffe():
    print("The drink is prepared!")

def wrong_drink(drink):
    if drink == "espresso":
        return False
    elif drink == "latte":
        return False
    elif drink == "cappuccino":
        return False
    elif drink == "americano":
        return False
    elif drink == "report":
        return False
    else:
        return True

lets_continue = True

while lets_continue:

    ## Automat
    user_choice = input("What can I get you? (espresso/latte/cappuccino/americano)\n")

    if wrong_drink(user_choice):
        print("Wrong choice! Try again!")
        pass
    else:
        # service report
        if user_choice == "report":
            password = input("Enter password.\n")
            print(report(int(password), rest_of_ingredients))
        else:
            # calculate ingredients 
            calculate_ingredients(user_choice)
            # check ingredients status
            lets_continue = out_of_ingredients(rest_of_ingredients["water"], rest_of_ingredients["milk"], rest_of_ingredients["coffee"])

        if lets_continue == False:
            break

        # user automat
        if user_choice == "espresso":
            sum = coins(user_choice)
            returnCoins(sum, user_choice)
        elif user_choice == "latte":
            sum = coins(user_choice)
            returnCoins(sum, user_choice)
        elif user_choice == "cappuccino":
            sum = coins(user_choice)
            returnCoins(sum, user_choice)
        elif user_choice == "americano":
            sum = coins(user_choice)
            returnCoins(sum, user_choice)

    

