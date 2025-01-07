import random


word_list=["aardvark","baboon","camel"]

chosen_word= random.choice(word_list)

placeholder=''

for letter in range(0,len(chosen_word)):
    placeholder+='_'


print(placeholder)

guess_list=[]
display=[]
number_of_lives=6

for letter in placeholder:
    display+=letter

while placeholder!=chosen_word and number_of_lives!=0:
    guess=input("Choose a letter bro:").lower()

    times_run=0
    for letter in chosen_word:
        
        if guess == letter :
            letter_index=chosen_word.index(guess,times_run,len(chosen_word))
            display[letter_index]=letter
        
        times_run+=1    

    if placeholder==''.join(display) and guess not in guess_list:
        number_of_lives-=1
        print(f"Ha Wrong, {guess} is not in the word.{number_of_lives} lives remaining ")
    
    elif placeholder==''.join(display) and guess in guess_list:
        print(f"Already guessed this, Guess again.\n{number_of_lives} lives remaining")
    else:
        print(f"Correct.{number_of_lives} lives remaining")
    
    placeholder=''.join(display)
 
    print(placeholder)
    guess_list+=guess
  
if placeholder==chosen_word:
    print('You win!')
elif number_of_lives==0:
    print(f"Game Over, You lose.\n The correct word was '{chosen_word}' ")
