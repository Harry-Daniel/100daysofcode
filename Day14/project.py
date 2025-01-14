from art import logo,vs
from data import data
import random

data_list=data
def random_choice(list):
    random_info=random.choice(list)
    return random_info

def remove_random_choice(list,element):
   item_index= list.index(element)
   list.pop(item_index)
   return list

def comparism(element):
    return f"{element["name"]}, a {element["description"]} , from {element["country"]}"

def more_followers(choice1,choice2):
    if choice1['follower_count']> choice2['follower_count']:
        return choice1
    return choice2


correct=True
score=0
guess=''
choice1={}
choice2={}
while correct:
    print(logo)
    if not score ==0:
        print(f"You are correct. You have {score} points")
    if score == 0:
        choice1= random_choice(data_list)
        data_list=remove_random_choice(data_list,choice1)
    else:
        choice1=choice2
    
    if data_list==[]:
        print("You've won the game")
        break
    choice2= random_choice(data_list)
    data_list=remove_random_choice(data_list,choice2)


    print(f"A. {comparism(choice1)}")
    print(vs)
    print(f"B. {comparism(choice2)}")

    guess=input("Who has more followers? Type A or B: ").lower()
    answer= more_followers(choice1,choice2)
    if guess=='a' and choice1 == answer:
        score+=1
    elif guess=='b' and choice2 == answer:
        score+=1
    else:
        print(f"You are wrong. Your score is {score} points. You lose")
        break


    

    if data_list==[]:
        print("You've won the game")
        break
    print("\n"*20)






    