#Secret Bidding System

import ascii
from ascii import logo
print(logo)
bidders_info = {}
winner = []
highest_bid= 0
bidding_finished = False
while not bidding_finished:
        
    name =input ("What is your name?: \n")
    bid = int(input ("What is your bid?: \n"))

    bidders_info[name] = bid
    print(bidders_info)
    valid_input = False
    while not valid_input:
        
        choice = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
        
        if choice == "no":
            bidding_finished = True
            valid_input = True
        elif choice == "yes":
            print("\n" *100)
            valid_input = True
        else:
            print("Incorrect input. 'Please Type again' \n")


for bidder in bidders_info:
    
    if bidders_info[bidder]> highest_bid:
        winner = [bidder]
        highest_bid = bidders_info[bidder]
    elif bidders_info[bidder] == highest_bid:
        winner.append(bidder)

if len(winner)==1: 
    print(f"winner is {winner[0]} with bid of {highest_bid}")
else:
    all_winners = " , ".join(winner)
    print(f"It's a tie! Winners are {all_winners} with a bid of {highest_bid}")
