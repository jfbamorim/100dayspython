################################################################
# Day 5 - Beginner - Python loops
################################################################
import random

#####################################################################
# Exercise 5.1 - Loops - Avg, Sum and length
#####################################################################
# 🚨 Don't change the code below 👇
#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#sum_height = 0
#nr_students = 0
#for height in student_heights:
#  sum_height += height
#  nr_students += 1
#print(str(round(sum_height / nr_students)))

#####################################################################
# Exercise 5.2 - Loops - High Score
#Instructions:
#You are going to write a program that calculates the highest score from a List of scores.
#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#The highest score in the class is: x
#####################################################################
# 🚨 Don't change the code below 👇
#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#bigger_score = 0
#for score in student_scores:
#  if score > bigger_score:
#    bigger_score = score
#print(f"The highest score in the class is: {bigger_score}")

#####################################################################
# 5.3 - FIZZ-BUZZ EXERCISE
#####################################################################
#Write your code below this row 👇
#number_range = range(1,101)
#for number in number_range:
#  if number % 3 == 0:
#    if number % 5 == 0:
#      print("FizzBuzz")
#    else:
#      print("Fizz")
#  elif number % 5 == 0:
#    print("Buzz")
#  else:
#    print(number)

#####################################################################
# 5.3 - FINAL PROJECT - DAY 5
#####################################################################

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
    #password += random.choice(letters)
    number = random.randint(0, len(letters) - 1)
    password += letters[number]

for j in range(0, nr_symbols):
    #password += random.choice(symbols)
    number = random.randint(0, len(symbols) - 1)
    password += symbols[number]

for k in range(0, nr_numbers):
    # password += random.choice(numbers)
    number = random.randint(0, len(numbers) - 1)
    password += numbers[number]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total = nr_letters + nr_symbols + nr_numbers
password_list = []

for i in range(0, nr_letters):
    password_list += random.choice(letters)
for i in range(0, nr_symbols):
    password_list += random.choice(symbols)
for i in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")
