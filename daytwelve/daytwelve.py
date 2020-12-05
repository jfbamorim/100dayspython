################################################################
# Day 12 - Beginner - Number Guessing Game 
################################################################
from random import randint
from daytwelve.number_guessing_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def start_game(input_attempts, input_surprise_nr):
    """Starts the game with the number of attempts"""
    end_game = False
    while input_attempts > 0 and not end_game:
        print(f"You have {input_attempts} remaining to guess the number.")
        guessed_nr = int(input("Make a guess:"))
        if guessed_nr == input_surprise_nr:
            print(f"You got it! The answer was {input_surprise_nr}")
            end_game = True
        elif guessed_nr < input_surprise_nr:
            print(f"Too low.")
        else:
            print(f"Too high.")
        input_attempts -= 1
        if input_attempts > 0:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose.")


# Main program
attempts = 0
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
surprise_nr = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = EASY_LEVEL_TURNS
elif difficulty == 'hard':
    attempts = HARD_LEVEL_TURNS
start_game(attempts, surprise_nr)
