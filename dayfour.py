# Banker Roulette Exercise - Who will pay the bill?
#import random
# 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

# Split string method
#namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
#names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bill_taker = random.randint(0, len(names)-1)
#name = names[bill_taker]
#print(f"{name} is going to buy the meal today!")

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
first_position = round(int(position)/10) - 1
second_position = round(int(position) % 10) - 1

map[second_position][first_position] = 'x'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
