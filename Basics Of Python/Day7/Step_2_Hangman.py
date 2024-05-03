import random
word_list = ["ardvark","baboon","camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word = random.choice(word_list)
blank = []
for i in word: blank += "_"
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
end_of_game = False
while "_" in blank:
    char = input("Guess a letter : ").lower()
    for i in range(len(word)):
        if word[i] == char:
            blank[i] = char
            
    if "_" not in blank:
        end_of_game = True
        print("You Win")
    # print(f"Current position {i}\nCurrent Letter : {word[i]}\nGuessed Letter : {char}")

# print(f"After guess {blank}")