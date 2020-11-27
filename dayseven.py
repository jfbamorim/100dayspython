####################################################################
# Day 7 - Hangman Project - Code re-arranged
####################################################################
# Step 1
import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
game_over = False
stages = hangman_art.stages
lives = 6

print(hangman_art.logo)

#Create an empty List called display.
display = []
for i in range(word_len):
    display.append("_")

while game_over == False and lives > 0:

#Ask the user to guess a letter and assign their answer to a variable
    char_choose = input("Guess a letter: ").lower()

#Check if the letter the user guessed is one of the letters in the chosen_word.
#for word in word_len:
#    print(char_choose == word)
    if char_choose not in chosen_word:
        lives -= 1
        print(f"You guessed {char_choose}, that's not in the word. You lose a life.")
    else:
        print(f"You've already guessed {char_choose}")

    for position in range(word_len):
        if char_choose == chosen_word[position]:
            display[position] = char_choose

    if "_" not in display:
        game_over = True

    print(f"{' '.join(display)}")
    print(stages[lives])

if lives == 0:
    print(f"You lose. The word we were looking for was {chosen_word}")

else:
    print("You won")