import random
from art import art
# Easy level has 10 attempts hard level has 5 attempts
print(art)



print("Welcome to the Number Guessing Game!")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
attempts=0
if difficulty== 'easy':
    attempts=10
elif difficulty =='hard':
    attempts=5
print(f"You have {attempts} attempts")
number=random.randint(1,100)

guess= int(input("Guess a number"))

def is_correct(guess):
    if guess == number:
        return f"You got it! The answer was {number}."
    elif guess < number:
        return f"You got it! The answer was {number}."

