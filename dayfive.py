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
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
bigger_score = 0
for score in student_scores:
  if score > bigger_score:
    bigger_score = score
print(f"The highest score in the class is: {bigger_score}")