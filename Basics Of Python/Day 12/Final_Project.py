import random

def check_answer(number,goal):
        if number < goal:
            print("Too Low. Guess Again.")
        elif number > goal:
            print("Too High. Guess Again.")
        else:
            print(f"You have won this Game. 😍 I guess number {goal}")
            return True

def start_guessing():
    print("Welcome to the Number Guessing Game!!! ")
    print("I am thinking of a number between 1 to 100")
    goal_num = random.randint(1,100)
    user_level = input("Choose a Difficulty level . 'easy' or 'hard' ")
    if user_level == 'easy':
        attempts = 10
        while attempts != 0:
            print(f"You have {attempts} remaining to guess number in game.")
            guess = int(input("Make a guess : "))
            if check_answer(guess,goal_num):
                break
            attempts -= 1
        if attempts == 0 and guess != goal_num:
            print("Oh no Your all attempts are gone !! You Lose :(")
            return
    else:
        attempts  = 5
        while attempts != 0:
            print(f"You have {attempts} remaining to guess number in game.")
            guess = int(input("Make a guess : "))
            if check_answer(guess,goal_num):
                break
            attempts -= 1
        if attempts == 0 and guess != goal_num:
            print("Oh no Your all attempts are gone !! You Lose :(")
start_guessing()