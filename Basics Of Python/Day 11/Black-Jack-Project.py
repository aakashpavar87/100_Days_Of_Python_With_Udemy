import random
import os
from Art import logo
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_with_card():
    '''This Function Returns a Random card From the Deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a Draw 😉"
    elif user_score == 0:
        return "You win with Black Jack 😎"
    elif computer_score == 0:
        return "Opponent win with Black Jack 😱"
    elif user_score > 21:
        return "You went over 21 😥"
    elif computer_score > 21:
        return "Oppenent went over 21 . You win 🤗"
    elif user_score > computer_score:
        return "Yeh you have win the game 🤩"
    else:
        return "Computer has won 👀"
    
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    
def play_game():
    '''This function is main play game function for black jack'''
    print(logo)
    
    is_game_over = False
    user = []
    computer = []
    
    for _ in range(2):
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    #computer_cards = []
        user.append(deal_with_card())
        computer.append(deal_with_card())
        
        
    while not is_game_over:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"Your cards : {user} And sum : {user_score} \n Dealer\'s Card : {computer[0]}")

        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            should_user_deal = input(f"Type 'y' for choosing another card or type 'n' for passing : ")
            if should_user_deal == 'y':
                user.append(deal_with_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer.append(deal_with_card())
        computer_score = calculate_score(computer)
        
    print(f"Your final hand : {user} and Your final score : {user_score}")
    print(f"Computer's final hand : {computer} and Computer's final score : {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')    
    play_game()
