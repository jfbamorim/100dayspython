# Banker Roulette Exercise - Who will pay the bill?
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill_taker = random.randint(0, names.__len__()-1)
name = names[bill_taker]
print(f"{name} is going to buy the meal today!")
