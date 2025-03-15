logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

# print(operations["*"](4, 8))

def calculator():
    print(logo)
    first_number = float(input("Type the first number:\n"))
    should_accumulate = True

    while should_accumulate:
        
        for symbol in operations.keys():
            print(symbol)
        operator = input("Type a mathematical operator:\n")
        second_number = float(input("Type a second number:\n"))

        final_result = operations[operator](first_number, second_number)

        print(f"{first_number} + {second_number} = {final_result}")

        choice = input("Do you want to continue with the previous result? Type y or n. \n").lower()

        if choice == 'y':
            first_number = final_result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()
    