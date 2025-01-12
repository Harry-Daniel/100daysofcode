from art import art
import random
# Once you go over 21 you lose instantly o matter what the house has
# First two cards are revealed and dealer reveals only one card 
#  You can choose to hit(Pick new cards )or stand(Stop picking)
# The goal is to have your cards closer to 21 or 21 directly compared to the house
# If the house picks and it's less than 17 the house picks again after you hold 
#  Ace can be either 11 or 1 depending on igf it's closer or further from 21

cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

# When game starts two cards are dealt each. 
play=True
start= input("Do you want to play a game of blackjack? y or n").lower()

if start== 'n':
    play=False


players_cards=[]
computers_card=[]
deal_cards=True


def hit():
    players_cards.append(random.choice(cards))
        
def player_cards_summary(cards):
    total=0
    for card in cards:
        total+=card
    print(f"Your cards are {cards}. Current Card Total: {total}")

def computer_cards_summary(cards):
    total=0
    for card in cards:
        total+=card
    print(f"Computer's cards are {cards}. Current Card Total: {total}")

def cards_total(cards):
    total=0
    for card in cards:
       total+=card     
    return total

def ace_is_1_or_11():
    if cards_total(players_cards)>21:
        for card in players_cards:
            if card== 11:
                card_index= players_cards.index(card)
                players_cards[card_index]=1

    
def win_status(computer_cards,player_cards):
    if 21-cards_total(computer_cards)<21-cards_total(player_cards):
        print("You Lose")
    elif 21-cards_total(player_cards)<21-cards_total(computer_cards):
        print("You win")

while play == True:
    print(art)
    for card in range(2):
        players_cards.append(random.choice(cards))
        computers_card.append(random.choice(cards))
    player_cards_summary(players_cards)
    print(f"Computer's cards are: {computers_card[0]}")

    if cards_total(players_cards) == cards_total(computers_card)==21:
        print(f"It's a tie ")
       

    elif cards_total(players_cards)==21:
        print(f"Congratulations, You win")
       
    
    else:
        while deal_cards == True and cards_total(players_cards)<21:
            
           
            draw=input("Would you like to draw another card? y for yes or n for no: ").lower()
        
            if draw=='n' :
                break
            elif draw=='y':
                players_cards.append(random.choice(cards))
                ace_is_1_or_11()
                player_cards_summary(players_cards)
                print(f"Computer's cards are: {computers_card[0]}")


    if cards_total(players_cards)>21:
        print("BUST! You lose")

    elif cards_total(players_cards)<21 and cards_total(computers_card)<17:
        computers_card.append(random.choice(cards))
    
    else :
        win_status(computers_card,players_cards)

    player_cards_summary(players_cards) 
    computer_cards_summary(computers_card)

    start=input("Want to play again ? y for yes, n for no: ").lower
    if start == 'n':
        play=False
    else:
        players_cards=[]
        computers_card=[]

    