#####################################################################
# Final Project - Blind Auction
#####################################################################
def find_high_bid(bidders):
    max_bid = 0
    for single_bid in bidders:
        if bidders[single_bid] > max_bid:
            name_bid_winner = single_bid
            max_bid = bidders[single_bid]
    print(f"The winning bidder was {name_bid_winner} with bid in value of ${max_bid}")


answer_bid = True
bidders = {}

while answer_bid:
    name_bid = input("What is your name: ")
    value_bid = int(input("What is your bid: $"))
    bidders[name_bid] = value_bid
    answer_bid = input("Is there any other user who wants to make a bid? Type yes or no").lower()
    if answer_bid == "no":
        answer_bid = False

find_high_bid(bidders)
