from Art import logo,vs
from Game_data import data
import random
import os


person_a = random.choice(data)
person_b = random.choice(data)
player_person = {}
score = 0
def start_game(personA,personB):
    os.system('cls')
    print(logo)
    article_a = ''
    if personA['description'][0] in ['A','E','I','O','U']:
        article_a = 'An'
    else:
        article_a = 'A'
    article_b = ''
    if personB['description'][0] in ['A','E','I','O','U']:
        article_b = 'An'
    else:
        article_b = 'A'
    print(f"Compare A : {personA['name']},{article_a} {personA['description']} from {personA['country']}")
    print(vs)
    print(f"Compare B : {personB['name']},{article_b} {personB['description']} from {personB['country']}")
def compare_follower(personA,personB,score):
    player_person = person_a
    if(personA['follower_count'] > personB['follower_count']):
        print(f"You win !!! Your Score is {score}")
        print(f"Your Player's Followers : {player_person['follower_count']} and opponent's followers : {personB['follower_count']}")
        # global score
        score += 1
        shuffle_b = random.choice(data)
        start_game(personB,shuffle_b)
        return False
    elif(player_person['follower_count'] < personB['follower_count']):
        # global score
        print(f"You Lose :( Your Final Score is : {score}")
        print(f"Your Player's Followers : {player_person['follower_count']} and opponent's followers : {personB['follower_count']}")
        return True
    else:
        print("It\'s a Draw 🙄")
        print(f"Your Player's Followers : {player_person['follower_count']} and opponent's followers : {personB['follower_count']}")
        return True
def continue_game(score):
    if(input("Enter A or B to select amongst above 2 Persons : ") == 'A'):
        if compare_follower(person_a,person_b,score) == True:
            return True
        # os.system('cls')
    else:
        if compare_follower(person_b,person_a,score) == True:
            return True
        
        # os.system('cls')
start_game(person_a,person_b)
continue_game(score=score)
end_of_game = False
while not end_of_game:
    if continue_game(score=score) == True:
        end_of_game = True