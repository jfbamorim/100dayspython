################################################################
# Day 11 - Beginner - The Blackjack Capstone Project
################################################################
import random
from blackjack_art import logo

############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    print(logo)

    #User play
    user_cards = deal_hand()
    user_score = calc_curr_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")

    #Dealer play
    dealer_cards = deal_hand()
    dealer_score = calc_curr_score(dealer_cards)
    print(f"Computer's first card: {dealer_cards[0]}")

    hit_me = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while hit_me == 'y':
        next_card = deal_one_card()
        user_cards.append(next_card)
        user_score = calc_curr_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if user_score <= 21:
            hit_me = input("Type 'y' to get another card, type 'n' to pass:").lower()
        else:
            compare_both_hands(user_cards, dealer_cards)

    while dealer_score < user_score:
        dealer_next_card = deal_one_card()
        dealer_cards.append(dealer_next_card)
        dealer_score = calc_curr_score(dealer_cards)

    compare_both_hands(user_cards, dealer_cards)


def deal_hand():
    your_cards = []
    first_card = deal_one_card()
    second_card = deal_one_card()
    your_cards.append(first_card)
    your_cards.append(second_card)
    return your_cards


def calc_curr_score(hand):
    sum_value = 0
    for card in hand:
        sum_value += card
    return sum_value


def deal_one_card():
    index = random.randint(0, 12)
    return cards[index]


def compare_both_hands(user_hand, dealer_hand):
    user_value = calc_curr_score(user_hand)
    dealer_value = calc_curr_score(dealer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_value}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_value}")

    if user_value > 21:
        print("You went over. You lose.")


# Main program:
answer = 'y'
while answer == 'y':
    answer = input("Do you want to play a game of Blackjack? Type y or n: ").lower()
    if answer == 'y':
        start_game()

##################### Hints #####################


#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



