# Open file in python
#file = open("my_file.txt")
# with open("my_file.txt") as file
# another option and dont need to close the file (it does automatically)

# Read file
#contents = file.read()
#print(contents)

# Close file - to free some resources
#file.close()

# Write to file : mode is by default read-only
#with open("new_file.txt", mode="w") as new_file:
#    #overwrite the file's content
#    new_file.write("New file & text via python.")

with open("new_file.txt", mode="a") as new_file:
    #overwrite the file's content
    new_file.write("\nNew text append via python.")

