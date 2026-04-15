import random
import art
print(art.logo)
"""
Our Blackjack Game House Rules

. The deck is unlimited in size.
. There are no jokers.
. The Jack/Queen/King all count as 10.
. The Ace can count as 11 or 1.
. Use the following list as the deck of cards:
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_cards(cards):
    """Returns a random card from the list"""
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    card3 = random.choice(cards)
    card4 = random.choice(cards)
    user_cards.append([card1, card2])
    computer_cards.append([card3, card4])
    return user_cards, computer_cards
    #print(user_cards, computer_cards)

def calculate_score(user_cards, computer_cards):
    """Returns the score of the cards"""
    user_score = 0
    computer_score = 0
    for card in user_cards:
        user_score += card
    for card in computer_cards:
        computer_score += card
    return (user_score, computer_score)


deal_cards(cards)
calculate_score(user_cards, computer_cards)






