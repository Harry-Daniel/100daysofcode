print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

direction = input("You're at a crossroads. Do you go left or right?")

if direction=='left':
    direction= input("You're at river.\n Do you swim or wait?")

    if direction== 'wait':
        direction=input("You reach an Island with 3 different colored doors.Which door do you take? Yellow, Red or Blue?")

        if direction=='Yellow':
            print("You Win!!")
        elif direction=='Red':
            print("You were burned by fire.\nGame Over.")
        elif direction=='Blue':
            print("You were eaten by beasts.\nGame Over.")
            
        else:
            print("Game Over")
    else:
        print("Attacked by trout.Game Over.")

else:
    print("You fall into a hole.\n Game Over")