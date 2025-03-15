ascii_hangman = """
 __   __  _______  __    _  _______  __   __  _______  __    _ 
|  | |  ||   _   ||  |  | ||       ||  |_|  ||   _   ||  |  | |
|  |_|  ||  |_|  ||   |_| ||    ___||       ||  |_|  ||   |_| |
|       ||       ||       ||   | __ |       ||       ||       |
|       ||       ||  _    ||   ||  ||       ||       ||  _    |
|   _   ||   _   || | |   ||   |_| || ||_|| ||   _   || | |   |
|__| |__||__| |__||_|  |__||_______||_|   |_||__| |__||_|  |__|
    
"""

print(ascii_hangman)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["apple", "meditation", "fruit", "chart", "travel", "aardvark"]
lives = 0

# Pick a random word
import random
random_word = random.choice(word_list)

# Generate a dashed line
placeholder = ""
for i in range(len(random_word)):
    placeholder += "_"

print("Guess: ", placeholder)

# result to check the final output

correct_letters = []
game_over = False
while not game_over:
    # Take user input
    guess = input("\n").lower()

    if guess in correct_letters:
        print("Already guessed ", guess)
        continue

    result = ""

    if guess not in random_word:

        print(HANGMANPICS[lives])
        lives += 1
        print(f"You guessed {guess}, that is not a letter in the word. You lose a life. Your remaining life {7 - lives}")
        if lives == 7:
            print(f"You lose! The chosen word was {random_word}.")

    for letter in random_word:
        if letter == guess:
            result += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            result += letter
        else:
            result += "_"
    print(result)



    if "_" not in result:
        print("You win!")
        game_over = True






# hangman = 0

# print("Start with any letter")
# while guess != random_word:
#     user_guess = input("")
#     if len(user_guess) > 1:
#         print("You can guess 1 letter at a time.")
#         continue
#     if user_guess not in random_word:
#         if hangman == 6:
#             print("Game Over")
#             break
#         else:
#             hangman += 1
#     word_index = random_word.index(user_guess)
#     guess = guess[:word_index] + user_guess + guess[word_index + 1:]
#     print("Guess: ", guess)