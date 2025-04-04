# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key":"value"}
# result = a_dict["non_existent_key"]

# IndexError
# fruit_list = [1,2,3,4]
# fruit = fruit_list[6]

# TypeError
# text = "abc"
# print(text + 5)

# Catching Exceptions
# try except else finally

# try:
#     code
# except:
#     if code errored out
# else:
#     if there were no exceptions
# finally:
#     no matter what happens

# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["asdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     print("There was an error")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

# raise

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# JSON
# json.load()
# json.dump()
# json.update