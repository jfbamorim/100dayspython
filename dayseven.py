####################################################################
# Day 7 - Hangman Project - Code re-arranged
####################################################################
# Step 1
import random
####################################################################
#ASCII for stages

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
display_has_no_blanks = word_len
lives = 6

print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = []
for i in range(word_len):
    display.append("_")

while display_has_no_blanks > 0 and lives > 0:

#Ask the user to guess a letter and assign their answer to a variable
    char_choose = input("Guess a letter: ").lower()

#Check if the letter the user guessed is one of the letters in the chosen_word.
#for word in word_len:
#    print(char_choose == word)
    if char_choose not in chosen_word and lives > 0:
        lives -= 1
        print(stages[lives])

    for position in range(word_len):
        if char_choose == chosen_word[position]:
            display[position] = char_choose
            display_has_no_blanks -= 1

if lives == 0 and display_has_no_blanks > 0:
    print("You lose")
else:
    print("You won")