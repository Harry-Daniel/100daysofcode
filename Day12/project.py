import random
from art import art
# Easy level has 10 attempts hard level has 5 attempts
print(art)

def is_correct(guess,attempts):
        if guess == number:
            
            return f"You got it! The answer was {number}."
        elif guess < number:
            return f"Your guess was too low, you have {attempts} left"
        elif guess > number:
            return f"Your guess was too high, you have {attempts} left"


print("Welcome to the Number Guessing Game!")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
attempts=0
if difficulty== 'easy':
    attempts=10
elif difficulty =='hard':
    attempts=5
print(f"You have {attempts} attempts")
number=random.randint(1,100)
guess= 120
while not guess == number and attempts>0:
    guess= int(input("Guess a number from 1- 100: "))
    # print(f"psttt number is {number}")
    if not guess ==number:
        attempts-=1

    print(is_correct(guess,attempts))

    if attempts==0:
        print(f"You have no attempts remaining, the number was {number}")
    

