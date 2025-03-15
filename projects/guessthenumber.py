import random
logo = r"""
 __    _     ____  __   __      _____  _     ____      _      _     _      ___   ____  ___  
/ /`_ | | | | |_  ( (` ( (`      | |  | |_| | |_      | |\ | | | | | |\/| | |_) | |_  | |_) 
\_\_/ \_\_/ |_|__ _)_) _)_)      |_|  |_| | |_|__     |_| \| \_\_/ |_|  | |_|_) |_|__ |_| \ 

"""

EASY_LEVEL = 10
HARD_LEVEL = 5

def guess_helper(guess, number_to_guess):
    if guess > number_to_guess:
        if guess - number_to_guess > 10:
            return "Too High"
        else:
            return "High"
    elif guess < number_to_guess:
        if number_to_guess - guess > 10:
            return "Too Low"
        else:
            return "Low"
    else:
        return "Correct"

restart = True
while restart: # loop to restart the game
    print(logo)
    print("Welcome to the Number Guess Game!")
    print("I'm thinking of a number between 1 and 100")
    print("Pssst, the correct answer is 68")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number_to_guess = random.randint(1, 101)
    
    if level.lower() == 'easy':
        # loop 10 times
        n = EASY_LEVEL

    else:
        # loop 5 times 
        n = HARD_LEVEL

    attempts = 0    
    while attempts < n:

        print(f"You have {n - attempts} remaining to guess the number")
        guess = int(input("Make a guess: "))
        result = guess_helper(guess, number_to_guess)
        print(result)
        if result == "Correct":
            break
        attempts += 1

        if attempts == n:
            print(f"You lose. The number was {number_to_guess}")

    if input("Press Q to Quit. Press any key to continue. \n").lower() == 'q':
        restart = False
    else:
        print("\n"*20)