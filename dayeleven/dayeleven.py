################################################################
# Day 11 - Beginner - The Blackjack Capstone Project
################################################################
import random
from blackjack_art import logo

############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    """Start the game"""
    print(logo)

    is_game_over = False
    # User play
    user_cards = deal_hand()
    user_score = calc_curr_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")

    # Dealer play
    dealer_cards = deal_hand()
    dealer_score = calc_curr_score(dealer_cards)
    print(f"Computer's first card: {dealer_cards[0]}")

    if user_score == 21 or dealer_score == 21:
        is_game_over = True

    hit_me = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while hit_me == 'y' and not is_game_over:
        next_card = deal_one_card()
        user_cards.append(next_card)
        user_score = calc_curr_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if user_score < 21:
            hit_me = input("Type 'y' to get another card, type 'n' to pass:").lower()
        else:
            break

    while dealer_score < user_score and dealer_score < 17 and not is_game_over:
        dealer_next_card = deal_one_card()
        dealer_cards.append(dealer_next_card)
        dealer_score = calc_curr_score(dealer_cards)

    compare_both_hands(user_cards, dealer_cards)


def deal_hand():
    """Return hands based on deal one card"""
    your_cards = []
    first_card = deal_one_card()
    second_card = deal_one_card()
    your_cards.append(first_card)
    your_cards.append(second_card)
    return your_cards


def calc_curr_score(hand):
    """Returns the current score of a player"""
    total_sum = sum(hand)
    if total_sum > 21:
        for card in hand:
            if card == 11:
                hand.remove(card)
                hand.append(1)
    return sum(hand)


def deal_one_card():
    """Returns a random card from the deck"""
    return random.choice(cards)


def compare_both_hands(user_hand, dealer_hand):
    """Comapre the hands between user and dealer"""
    user_value = calc_curr_score(user_hand)
    dealer_value = calc_curr_score(dealer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_value}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_value}")

    if user_value > 21:
        print("You went over. You lose.")
    elif dealer_value > 21:
        print("Opponent went over. You win.")
    elif user_value == 21:
        print("Win with a Blackjack.")
    elif dealer_value == 21:
        print("Lost to a Blackjack.")
    elif user_value == dealer_value:
        print("You tied.")
    elif user_value > dealer_value:
        print("You won.")
    else:
        print("You lost.")
    return


# Main program:
answer = 'y'
while answer == 'y':
    answer = input("Do you want to play a game of Blackjack? Type y or n: ").lower()
    if answer == 'y':
        start_game()


#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
