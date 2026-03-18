import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock, paper, scissors]

player1 = input("Rock, paper, or scissors: ").lower()

if player1 == "rock":
    player1 = rock
elif player1 == "paper":
    player1 = paper
elif player1 == "scissors":
    player1 = scissors
else:
    print("Invalid choice.")
    exit()

player2 = RPS[random.randint(0,2)]

print("Player1 chose: ", player1)
print("Player2 chose: ", player2)

if player1 == player2:
    print("Tie")
elif player1 == rock and player2 == scissors:
    print("Player 1 wins!")
elif player1 == scissors and player2 == paper:
    print("Player 1 wins!")
elif player1 == paper and player2 == rock:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")




