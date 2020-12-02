################################################################
# Day 13 - Beginner - Debugging and fixing errors in code
################################################################
############DEBUGGING#####################

# Describe Problem
def my_function():
    # DEBUGGED - IT NEVER REACHES 20 because range go from 0 to 19.
    # for i in range(1, 21) -> solution
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# DEBUGGER - it gaves index_error -> index out of bounds because sometimes it tries to retrieve
# data from dice_imgs list at index 6
# dice_num = randint (0,5) -> solution
# Other soltion is print(dice_imgs[dice_num-1])
print(dice_imgs[dice_num])

# Play Computer
# DEBUGGED - When year is 1994 it does not print anything at all
year = int(input("What's your year of birth?"))
# missing equal on comparison with 1994
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the Errors
# Every input come as string, so when dealing with integer value, cast is needed.
# age = int(input("How old are you?"))
age = input("How old are you?")
if age > 18:
#error in print - identation
#print("You can drive at age {age}.")
    # Fixed
    print("You can drive at age {age}.")


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])