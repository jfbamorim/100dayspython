################################################################
# Day 2 - Beginner - Understanding data types
################################################################
#My solution
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
bill = float(bill) * ((1/float(tip)) + 1)
total_person = round(float(bill) / int(people), 2)
print(f"Each person should pay: {total_person}")

# Teacher solution
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60
#print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#people = int(input("How many people to split the bill?"))

#long form
#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill + total_tip_amount
#bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)

#short form
#final_amount = round(bill * (1 + tip / 100) / people, 2)

#print(f"Each person should pay: ${final_amount}")