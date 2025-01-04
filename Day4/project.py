import random
rock='''
        _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)

          '''

paper='''
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
          '''

scissors='''
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)

          '''

computer_choices=[0,1,2]


user_choice=int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))





computer_choice=random.choice(computer_choices)

if 0<=user_choice<=2:
    if user_choice== 0:
        print(rock)
    elif user_choice== 1:
        print(paper)
    elif user_choice== 2:
        print(scissors)

    print("Computer chose:")
    if computer_choice== 0:
        print(rock)
    elif computer_choice== 1:
        print(paper)
    elif computer_choice== 2:
        print(scissors)

    if computer_choice==0 and user_choice==2:
        print("You lose")
    elif computer_choice==1 and user_choice==0:
        print("You lose")
    elif computer_choice==2 and user_choice==1:
        print("You lose")
    elif computer_choice==user_choice:
        print("You draw")
    else:
        print("You win")
else:
    print('You typed in an invalid input.')