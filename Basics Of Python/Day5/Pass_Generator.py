# #Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
demo = []
password = ""
size = nr_letters + nr_numbers + nr_symbols
for i in range(nr_letters):
    idx1 = random.randint(0, len(letters) - 1)
    demo += letters[idx1]

for i in range(nr_numbers):
    idx2 = random.randint(0, len(numbers) - 1)
    # idx1 = random.randint(0,len(letters)-1)
    demo += numbers[idx2]

for i in range(nr_symbols):
    idx3 = random.randint(0, len(symbols) - 1)
    # idx1 = random.randint(0,len(letters)-1)
    demo += symbols[idx3]

# for i in range(0,len(demo)-1):
#     password += demo[random.randint(i,len(demo)-1)]
print(f"Your Password is : {demo}")
random.shuffle(demo)
for i in demo:
    password += i
print(f"Your Password is : {password}")
if True:
    print("Hello")
