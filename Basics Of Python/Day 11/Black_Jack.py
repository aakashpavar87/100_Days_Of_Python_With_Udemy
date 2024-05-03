from Art import logo
import os
import random
play = input("Do you want to play the  Black Jack Game [Y/N]: ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
player_card_1 = random.choice(cards)
player_card_2 = random.choice(cards)
user.append(player_card_1)
user.append(player_card_2)

def result():
    print()
    
def deal_with_card(user):
    sum_of_user_card = sum_of_cards(user)
    if sum_of_user_card < 21:
        next_card = input("Do you want to choose another Random Card [Y/N]: ").lower()
        if next_card == 'y':
            user.append(random.choice(cards))
            print(f"Now you have these cards {user} and total {sum_of_cards(user)}")
            deal_with_card(user)
        else:
            result()
    else:
        print("Oops ! You lose the game because you got points over 21")
        return
        
    return user

def sum_of_cards(cards):
    sum = 0
    for point in cards:
        sum += point
    return sum

def dealer_plays(cards):
    computer_card_1 = random.choice(cards)
    computer.append(computer_card_1)
    
    
if play == 'y':
    os.system('cls')
    print(logo)
    print(f"Your Cards: {user}, Current Score : {sum_of_cards(user)}")