import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("Choose your option 0 for Rock, 1 for Paper and 2 for Scissors : "))

print(f"You choose {player_choice}")
if player_choice == 0:
    print(f"{rock}")
elif player_choice == 1:
    print(f"{paper}")
else:
    print(f"{scissors}")

computer_choice = random.randint(0,2)
print(f"Computer Choose {computer_choice}")
if computer_choice == 0:
    print(f"{rock}")
elif computer_choice == 1:
    print(f"{paper}")
else:
    print(f"{scissors}")
    
if player_choice == computer_choice :
    print("It\'s a Draw")
elif ((player_choice == 0) and (computer_choice == 2)) or ((player_choice == 2) and (computer_choice == 1)) or ((player_choice == 1) and (computer_choice == 0)):
    print("You Win")
else:
    print("You Lose")