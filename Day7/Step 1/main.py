import random

word_list=["aardvark","baboon","camel"]

chosen_word= random.choice(word_list)

print(chosen_word)

guess=input("Choose a letter bro:\n").lower()



for letter in chosen_word:
    if guess == letter:
        print("Right")
    elif guess != letter:
        print("Wrong")
