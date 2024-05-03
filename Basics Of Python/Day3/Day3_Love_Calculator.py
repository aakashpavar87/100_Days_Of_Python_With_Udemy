name1 = input("Enter your name : ")
name2 = input("Enter their Name : ")
combined_name  = name1 + name2
combined_name_lower = combined_name.lower()
t = combined_name_lower.count('t')
r = combined_name_lower.count('r')
u = combined_name_lower.count('u')
e = combined_name_lower.count('e')
true = t+r+u+e
l = combined_name_lower.count('l')
o = combined_name_lower.count('o')
v = combined_name_lower.count('v')
e = combined_name_lower.count('e')
love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score <= 90) and (love_score > 85) :
    print(f"Your love score is {love_score}, you both will live together.")
elif (love_score <= 85) and (love_score > 65) :
    print(f"Your love score is {love_score} you are great with each other")
else:
    print(f"Your love score is {love_score}")