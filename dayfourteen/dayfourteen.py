################################################################
# Day 14 - Beginner - Higher or lower game 
# Who was more followers on Instagram?
################################################################
from dayfourteen.higher_or_lower_art import logo, vs
from dayfourteen.higher_or_lower_dat import data
import random


def format_data(account):
    """Format account into printable format: name, description and country"""
    person_name = account["name"]
    person_description = account["description"]
    person_country = account["country"]
    return f"{person_name}, a {person_description}, from {person_country}"


def get_random_character():
    """ Get random person from dictionary data """
    new_character = random.choice(data)
    return new_character


def compare(person_one, person_two):
    if person_one["follower_count"] > person_two["follower_count"]:
        return "a"
    else:
        return "b"


def start_game():
    print(logo)
    print("Guess who was more followers on Instagram!")
    game_over = False
    score = 0

    person_one = get_random_character()
    person_two = get_random_character()
    while person_one == person_two:
        person_two = get_random_character()
    while not game_over:
        print(format_data(person_one))
        print(vs)
        print(format_data(person_two))
        answer = input("Whom's your choice? ").lower()
        if answer == compare(person_one, person_two):
            score += 1
            print(f"You get this one right! Your current score is {score}")
            if answer != 1:
                person_one = person_two
            person_two = get_random_character()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


start_game()
