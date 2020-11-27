####################################################################
# Day 7 - Hangman Project - Code re-arranged
####################################################################
# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
display_has_no_blanks = word_len
print(f'Pssst, the solution is {chosen_word}.')

#TODO-2.1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for i in range(word_len):
    display.append("_")

#TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while display_has_no_blanks > 0:

#TODO-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    char_choose = input("Guess a letter: ").lower()

#TODO-1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#for word in word_len:
#    print(char_choose == word)

#TODO-2.2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_len):
        if char_choose == chosen_word[position]:
            display[position] = char_choose
            display_has_no_blanks -= 1

#TODO-2.3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
# replace with "_".
    print(display)
    print(display_has_no_blanks)
print("You won")