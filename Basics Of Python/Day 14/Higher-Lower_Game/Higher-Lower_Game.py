from Art import logo,vs
from Game_data import data
import random
import os

#Display formatted message to player
def format_data(account):
    '''Formats Data chosen from Game Data File.'''
    account_name = account['name']
    account_desc = account['description']
    account_ctr = account['country']
    return f"{account_name}, a {account_desc} from {account_ctr}"

def check_answer(guess,a_followers,b_followers):
    '''This checks both account's followers '''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

#print data which chosen    
print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = False

while not game_should_continue:
    #choose two random data dictionaries
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    #Ask Player for greater follower
    guess = input("Who has more followers ? Type 'A' or 'B' : ").lower()

    #Check if user is correct
    ##Get follower count of each account 
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    
    #clear the screen 
    os.system('cls')
    print(logo)
    ##Use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You're right your current score is : {score}.")
    else:
        game_should_continue = True
        print(f"Sorry you're wrong . Final Score is {score}.")

