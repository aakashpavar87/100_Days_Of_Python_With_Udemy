import os
from Art import logo
print(logo)
auction = {}
end_program = False
while not end_program:
    bidder = input("Enter your Name : ")
    bid = int(input("Enter your bid ? $"))
    auction[bidder] = bid
    end = input("Is there any other bidder (Y/N): ").lower()
    if end == 'y':
        os.system('cls')
    else:
        end_program = True
        # os.system('cls')
def find_winner(bids):
    max = 0
    max_bidder = ''
    for key in bids:
        if bids[key] > max:
            max = bids[key]
            max_bidder = key
    print(f"Winner of the auction is {max_bidder} with bid of {bids[max_bidder]}")
end_screen = False
while not end_screen:
    find_winner(auction)
    choice = input("Do you want to exit the auction : (Yes/No)").lower()
    if choice == 'yes':
        end_screen = True
        print("*******Thank you for coming in auction***********")