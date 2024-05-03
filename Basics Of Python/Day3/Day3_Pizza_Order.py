print("Weclome to python  pizza deliveries !")
size = input("what size pizza do you want ? S, M or L : ")
add_peproni = input("Do yuo want to add peproni ? Y or N : ")
add_cheeze = input("Do you want to add extra Cheeze ? Y or N : ")
#S $15,M $20,L $25
#S pep $2 or $3
#cheeze $1
price = 0
if(size == 'S'):
    price += 15
elif(size == 'M'):
    price += 20
elif(size == 'L'):
    price += 25

if add_peproni == 'Y':
    if size == 'S':
        price += 2
    else :
        price += 3

if add_cheeze == 'Y':
    price += 1
    
print(f"Your total bill : ${price}")