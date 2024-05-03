print("Welcome to the tip calculator.")
bill_amount = (float)(input("What was the total bill ? $"))
interest_rate = (float)(input("what percentage would you like to give :10, 12 or 15 ?  "))
people_split = (float)(input("How many people to split the bill ? "))
total_bill_amount = bill_amount + (bill_amount*(interest_rate/100))
separate_amount = total_bill_amount/people_split
print(f"Each person should pay : {round(separate_amount,2)}");