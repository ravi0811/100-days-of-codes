import random
from ascii import logo, vs
from game_data import data


# This function handles the end-of-game logic and checks if the user wants to restart.
def repeat():
    play_again= input("Do you want to play again> 'Yes' or 'no':\n").lower()
    if play_again== "yes":
        play_game()
    elif play_again == "no":
        print("Thank you, goodbye!")
    else:
        print("Invalid input, Try again")
        repeat()
        
#----- main funtion----
def play_game():
    print(logo)
    game_on= True
    score=0
    data1 = []
    data2= []

    while game_on:

        if score ==0:
            data1= random.choice(data)
            data2= random.choice(data)
            
        else:
            data1= data2
            data2= random.choice(data)
            
        while data1==data2:
            data2= random.choice(data)

        a= data1["follower_count"]
        b= data2["follower_count"]

        if score>0:
            print("\n"*10)
        print(f"Compare A: {data1['name']} , {data1['description']} , {data1['country']}")
        print(vs)
        print(f"Compare B:- {data2['name']} , {data2['description']} , {data2['country']}")
        
        user_choice= input("Who has more followers 'A' or 'B'\n").lower()

        if user_choice== "a" and a>b:
            score+=1
            print(f"Your Score= {score}")
        elif user_choice=="b" and a<b:
            score+=1
            print(f"Your Score= {score}")
        else:
            print(f"Game over, Score= {score}")
            game_on= False
            repeat()
play_game()
