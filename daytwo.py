print("Welcome to the tip calculator")
print("What was the total bill?")
bill = input()
print("What was the percentage tip would you like to give? 10, 12 or 15?")
tip = input()
bill = float(bill) * ((1/float(tip)) + 1)
print(bill)
print("How many people to split the bill?")
people = input()
total_person = round(float(bill) / int(people), 2)
print(f"Each person should pay: {total_person}")
