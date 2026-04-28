from random import randint
from game_data import data
from art import *

choice1 = randint(0, 49)
choice2 = randint(0, 49)

print(f"Compare A: {data[choice1]['name']}, a {data[choice1]['description']} from {data[choice1]['country']}")
print(f"Against B: {data[choice2]['name']}, a {data[choice2]['description']} from {data[choice2]['country']}")

answer = input("Who has more followers? Type 'A' or 'B': ").lower()

score = 0

if answer == 'a':
    if data[choice1]['follower_count'] > data[choice2]['follower_count']:
        print(f"You are right! Current score: {score + 1}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
elif answer == 'b':
    if data[choice2]['follower_count'] > data[choice1]['follower_count']:
        print(f"You are right! Current score: {score + 1}.")
    else:
        print(f"Sorry, that's wrong.  Final score: {score}.")