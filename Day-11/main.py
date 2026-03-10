import random
from ascii import logo

def play_game():
    print(logo)
    #Black jack
    number = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

    #-----Computer Section-----
    computer_total_score =0

    computer_score1=[]
    for num in range(2):
        score = random.choice(number)
        computer_score1.append(score)
        computer_total_score +=score
    print(f"Computer Score = {computer_score1[0]}\n\n\n")
    if computer_score1[0] == 11 and computer_score1[1]==11:
        computer_score1[1]=1
        computer_total_score = 12

    #-----User Section-----


    #----- Getting the first two card numbers-----
    user_score =[]
    user_total_score =0
    for num in range(2):
        rand_num = random.choice(number)
        user_total_score += rand_num
        user_score.append(rand_num)
    if user_score[0]==11 and user_score[1]==11:
        user_score[1]=1
        user_total_score=12
        
    print(f"User Cards = {user_score}")
    print (f"User Score = {user_total_score}\n\n") 

    if user_total_score == 21:
        print("Blackjack! You win instantly!")
        game_on = False # Skips the hit/stand phase
    #-----User Choice-----
    game_on = True

    while game_on:
        user_input = input('Press "H" to Hit again and "S" To Stand\n').lower()
        if user_input =="h":
            sub_score = random.choice(number)
        
            if sub_score == 11 and sub_score + user_total_score > 21:
                sub_score = 1

            
            user_total_score += sub_score
            user_score.append(sub_score)

            if user_total_score >21:
                print(f"You Lose. {user_score} total score= {user_total_score}")
                
                break

            print(user_score)
            print(user_total_score)
        elif user_input == "s":
            game_on = False
            dealer_bust = False  # Initialize here to avoid NameError

            # -----Dealer's Turn-----
            while computer_total_score < 17:
                comp_card = random.choice(number)
                if comp_card == 11 and computer_total_score + comp_card > 21:
                    comp_card = 1
                
                computer_total_score += comp_card
                computer_score1.append(comp_card)
                
                if computer_total_score > 21:
                    print(f"Dealer busted with {computer_total_score}! You win!")
                    dealer_bust = True
                    break

            # -----Final Comparison-----
            # Only compare scores if the dealer is still in the game
            if not dealer_bust:
                print(f"\nFinal Scores - You: {user_total_score}, Dealer: {computer_total_score}")
                print(f"Dealer's Cards: {computer_score1}")
                
                if user_total_score > computer_total_score:
                    print("You win! ")
                elif user_total_score < computer_total_score:
                    print("You lose! ")
                else:
                    print("It's a tie! ")
            
            break # Exit the while game_on loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
