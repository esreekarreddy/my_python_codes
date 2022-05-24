############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo

def deal_card():
    """ Returns a random card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_of_cards):
    """ Returns sum of the card values """
    score = sum(list_of_cards)
    if len(list_of_cards) == 2 and (score == 21):
        return 0
    elif (11 in list_of_cards) and (score > 21):
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return score

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Computer wins, computer has a blackjack"
    elif user_score == 0:
        return "You win, you have a blackjack"
    elif user_score > 21:
        return "You crossed 21, you lose."
    elif computer_score > 21:
        return "Computer crossed 21, you win"
    elif user_score > computer_score:
        return "You win..."
    else:
        return "You lose..."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Do you want to draw another card(yes/no)? ").lower()
            if user_deal == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards are {user_cards} and your score is {user_score}")
    print(f"Computer cards are {computer_cards} and computer score is {computer_score}")
    print(compare(user_score, computer_score))

    new_game = input("Do you want to play again(yes/no)? ")
    while new_game == "yes":
        os.system("clear")
        play_game()
    
    print("Thnaks for playing.")
    exit()
play_game()

