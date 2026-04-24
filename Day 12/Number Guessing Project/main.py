from random import randint
import art
print(art.logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        exit()

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
answer = randint(1,100)

print(f"Pssst, the correct answer is {answer}")
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))
check_answer(guess, answer)






