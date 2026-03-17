#-----Coffee Machine-----

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

def make_coffee(user):
    for items in resources:
        if items in MENU[user_choice]["ingredients"]:
            resources[items]-= MENU[user_choice]["ingredients"][items]


def is_suffecient(user):
    '''checks if resource is sufficient or not and return value'''
    for items in MENU[user]["ingredients"]:
        if resources[items]<MENU[user]["ingredients"][items]:
            return(f"{items} is not sufficient")
        
    return True
        
def process_coins():
    '''takes coins form user and convert it in dollors'''
    quarters= int(input("How many quarters?:"))*0.25
    dimes= int(input("How many dimes?:"))*0.10
    nickles=int(input("How many nickles?:"))*0.05
    pennies=int(input("How many pennies?:"))*0.01

    dollars=quarters+dimes+nickles+pennies
    change= round(dollars- MENU[user_choice]["cost"],2)
    if dollars==MENU[user_choice]["cost"]:
        print("Here is your coffee🍵 enjoy.")
        make_coffee(user_choice)
    elif dollars>MENU[user_choice]["cost"]:
        print(f"Here is your {change}$ change.")
        print(f"Here is your {user_choice}🍵 enjoy.")
        make_coffee(user_choice)
    elif dollars< MENU[user_choice]["cost"]:
        print("Sorry thats not enough money. Money refunded")

        
machine_on=True

while machine_on:

    user_choice=input("What would you like? (espresso/latte/cappuccino):")


    
    if user_choice== "espresso" or user_choice=="latte" or user_choice=="cappuccino":
        resources_sufficient=is_suffecient(user_choice)
        if resources_sufficient==True:
            process_coins()

        else:
            print(resources_sufficient)


    elif user_choice=="report":
        print(resources)

    elif user_choice=="off":
        machine_on=False       

