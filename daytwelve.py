################################################################
# Day 12 - Beginner - Number Guessing Game
################################################################
import random
from number_guessing_art import logo


def start_game(attempts, surprise_nr):
    end_game = False
    while attempts > 0 and not end_game:
        print(f"You have {attempts} remaining to guess the number.")
        guessed_nr = int(input("Make a guess:"))
        if guessed_nr == surprise_nr:
            print(f"You got it! The answer was {surprise_nr}")
            end_game = True
        elif guessed_nr < surprise_nr:
            print(f"Too low.")
            print(f"Guess again.")
        else:
            print(f"Too high.")
            print(f"Guess again.")
        attempts -= 1


# Main program
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
surprise_nr = random.randint(1, 100)
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
start_game(attempts, surprise_nr)
