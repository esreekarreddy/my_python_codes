import os
from random import choice
from art import logo, vs
from data import data

score = 0 
def compare(pick_a, pick_b, user_input):
    """ Takes picks and user input to compare and find if user is correct or not"""
    global score
    followers_a = pick_a["follower_count"]
    followers_b = pick_b["follower_count"]
    if user_input == "a" and followers_a > followers_b:
        score += 1
        pick = pick_a
    elif user_input == "b" and followers_b > followers_a:
        score += 1
        pick = pick_b
    else:
        os.system("clear")
        print(logo)
        print(f"You lose, your score is {score}.")
        return
    os.system("clear")
    print(logo)
    print(f"Currently your score is {score}")
    user_pick(pick)

def user_pick(pick):
    pick_a = pick
    pick_b = choice(data)
    if pick_a == pick_b:
        pick_b = choice(data)
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']} ")
    print(vs)
    print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']} ")
    user_input = input("Guess who has more followers? Type 'A' or 'B': ").lower()
    compare(pick_a, pick_b, user_input)

pick_a = choice(data)
user_pick(pick_a)