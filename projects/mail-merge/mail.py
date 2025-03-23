PLACEHOLDER = "[name]"

# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter:
#     letter_contents = letter.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
        

with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names_file:
        letter_contents = letter.read()
        names = names_file.readlines()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, name)
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
                completed_letter.write(new_letter)
