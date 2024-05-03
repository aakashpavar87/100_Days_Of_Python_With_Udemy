import random
word_list = ["ardvark","baboon","camel"]
word = random.choice(word_list)
char = input("Guess a letter : ")
print(word)
for i in range(len(word)):
    if word[i] == char:
        print("Right")
    else :
        print("Wrong")
