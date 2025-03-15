# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else: 
#     bill += 25

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is : ${bill}")

print("""Welcome to Treasure Island\nYour mission is to find the treasure""")
direction = input("left or right?\n")

if direction.lower() == "right":
    print("Game Over.")
elif direction.lower() == "left":
    action = input("swim or wait?\n")
    if action.lower() == "swim":
        print("Game Over.")
    elif action.lower() == "wait":
        door = input("blue or red or yellow door?\n")
        if door.lower() == "red" or door.lower() == "blue":
            print("Game Over.")
        elif door.lower() == "yellow":
            print("You win!")
        else:
            print("Invalid Input.")
    else:
        print("Invalid Input.")
else:
    print("Invalid Input.")
