import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

# Create a dictionary {"A": "Alpha"}

phonetic = {row.letter: row.code for index, row in data.iterrows()}

word = input("Input a word: \n")


result = [phonetic[char.upper()] for char in word]

print(result)