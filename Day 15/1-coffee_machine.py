from art import logo
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(Money, 2)}")


Money=0.0
game_is_true = True
print(logo)
while game_is_true:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        get_report()
    if user_input == "latte" or user_input == "cappuccino" or user_input == "espresso":
        if(resources['water']<MENU[user_input]['ingredients']['water']):
            print("Sorry there is not enough water")
            continue
        if(resources['coffee']<MENU[user_input]['ingredients']['coffee']):
            print("Sorry there is not enough coffee")
            continue
        if (user_input == "latte" or user_input == "cappucino") and resources['milk']<MENU[user_input]['ingredients']['milk']:
            print("Sorry there is not enough milk")
            continue
        if(Money<MENU[user_input]['cost']):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            Money=Money+0.25*quarters+dimes*0.10+nickles*0.05+pennies*0.01
            if(Money<MENU[user_input]['cost']):
                print("Sorry that's not enough money. Money refunded.")
                continue
        Money-=MENU[user_input]["cost"]
        resources['water']-=MENU[user_input]['ingredients']['water']
        resources['coffee']-=MENU[user_input]['ingredients']['coffee']
        if(user_input=="latte" or user_input=="cappuccino"):
            resources['milk']-=MENU[user_input]['ingredients']['milk']
        
        print(f"Here is ${round(Money, 2)} in change")
        print(f"Here is your {user_input}☕ Enjoy!")

            