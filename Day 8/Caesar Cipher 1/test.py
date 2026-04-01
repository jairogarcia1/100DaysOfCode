""""You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.



e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3  """


def calculate_love_score(name1, name2):
    for char in name2:
        if char in name1:
            print(f"{char} occurs {name1.count(char)} time(s) in {name1}")

calculate_love_score("Kanye West", "Kim Kardashian")