import random
names_string = input("Enter name of persons separated by a comma : ")
names = names_string.split(', ')
# print(f"Today\'s bill will be paid by {names[random.randint(0,len(names)-1)]}")
print(f"Today\'s bill will be paid by {random.choice(names)}")

