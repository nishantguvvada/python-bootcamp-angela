print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
total_tip = 1 + (tip/100)
people = int(input("How many people to split the bill?\n"))

pay_per_person = (total_bill * total_tip) / people

print(f"Each person should pay: ${round(pay_per_person, 2)}")