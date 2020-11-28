####################################################################
# Day 9 - Beginner - Dictionaries and nesting
####################################################################
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#Retrieve data from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through an dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])