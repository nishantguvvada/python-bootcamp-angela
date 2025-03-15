rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
import random
computer_choice = random.randint(0,2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= user_input <= 2:
    print("Your move:\n", choices[user_input])
    print("Computer chose:\n", choices[computer_choice])
    if user_input == computer_choice:
        print("Draw")
    elif user_input == 0 and computer_choice == 1:
        print("You lose")
    elif user_input == 1 and computer_choice == 2:
        print("You lose")
    elif user_input == 2 and computer_choice == 0:
        print("You lose")
    else:
        print("You win")
else:
    print("Invalid input!") 
