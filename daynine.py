####################################################################
# Day 9 - Beginner - Dictionaries and nesting
####################################################################
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
# Retrieve data from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through an dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

####################################################################
# New exercise:

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆


student_grades = {}

grade = 0
score = ""
for student in student_scores:
    grade = student_scores[student]
    if 100 >= grade > 90:
        score = "Outstanding"
    elif 90 >= grade > 80:
        score = "Exceeds Expectations"
    elif 80 >= grade > 70:
        score = "Acceptable"
    else:
        score = "Fail"
    student_grades[student] = score

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting Dictionary in a Dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuggart"], "total_visits": 4}
}

# Nesting Dictionary in a List:
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuggart"],
        "total_visits": 4
    }
]