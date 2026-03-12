#Number guessing game
import random
from ascii import logo
print(logo)
#-----Computer Generated Random Number-----
# Generate a random target number between 1 and 100
random_num = random.randint(1,100)


# Display the welcome message with title casing
print("Welcome to the number guessing game!".title())
print("I am guessing a number between 1 and 100.")

# Get difficulty level and convert to lowercase to avoid case-sensitivity errors
difficulty= input("Choose the difficulty, Type 'easy' or 'hard':\n").lower()

# Set the number of attempts (lives) based on the chosen difficulty
if difficulty == "easy":
    lives = 10
else:
    # Default to 5 lives for 'hard' or any other input
    lives = 5

# Start the game loop; continues as long as the player has lives left
while lives!=0:

    user_guess= int(input("Enter the number you guess:\n"))

    # Check if the guess matches the computer's number
    if user_guess == random_num:
        print("You win.")
        break
    else:
        lives-=1
        if lives!=0:
            if user_guess > random_num:
                print("Too High\nGuess again.")
            else:
                print("Too Low\nGuess again.")
            print(f"you have {lives} attempt remaining to guess the number.")

# Final check: If the loop ends and lives are 0, the player loses
if lives== 0:
    print(f"You lose. The number was {random_num}.")
