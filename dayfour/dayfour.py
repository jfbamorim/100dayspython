########################################################
# Day 4 - Beginner - Random & Python lists
# Banker Roulette Exercise - Who will pay the bill?
########################################################
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

########################################################
# Treasure Map
########################################################

# 🚨 Don't change the code below 👇
#row1 = ["⬜️","⬜️","⬜️"]
#row2 = ["⬜️","⬜️","⬜️"]
#row3 = ["⬜️","⬜️","⬜️"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#first_position = round(int(position)/10) - 1
#second_position = round(int(position) % 10) - 1

#map[second_position][first_position] = 'x'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
#print(f"{row1}\n{row2}\n{row3}")

########################################################
# Final day project
########################################################
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Lets play Rock, Paper, Scissors")
shot = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors:\n"))

if shot == 0:
  print("Your choice:\n" + rock)
elif shot == 1:
  print("Your choice:\n" + paper)
else:
  print("Your choice:\n" + scissors)

pc_shot = random.randint(0, 2)

if pc_shot == 0:
    print("PC choice:\n" + rock)
elif pc_shot == 1:
    print("PC choice:\n" + paper)
else:
    print("PC choice:\n" + scissors)

if pc_shot == shot:
    print("Tied game")
else:
    if (pc_shot == 0 and shot == 1) or (pc_shot == 1 and shot == 2) or (pc_shot == 2 and shot == 0):
        print("You win")
    else:
        print("You lose")