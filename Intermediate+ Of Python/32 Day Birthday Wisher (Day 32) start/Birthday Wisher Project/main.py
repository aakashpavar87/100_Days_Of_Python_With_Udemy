##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib as sm
import pandas
import datetime as dt
import random

with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter:
    cur_letter = letter.readlines()


today = dt.datetime.today()
today_month = today.month
today_day = today.day
today_tup = (today_month, today_day)
MY_MAIL = "aakashpavar87@gmail.com"
MY_PASS = "cwdfzwgskdqvquwf"

dob_data = pandas.read_csv("birthdays.csv")
dob_month = dob_data.month.to_list()
dob_day = dob_data.day.to_list()

birthday_dict = {(row.month, row.day): row for (index, row) in dob_data.iterrows()}

print(birthday_dict[today_tup])
if today_tup in birthday_dict:
    fr_mail = birthday_dict[today_tup]["email"]
    fr_name = birthday_dict[today_tup]["name"]
    cur_letter[0] = cur_letter[0].replace("[NAME]", fr_name)
    letter_msg = "".join(cur_letter)
    letter_msg = "Subject: Happy Birthday Wish\n\n" + letter_msg

    print(letter_msg)
    with sm.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=fr_mail,
                            msg=f"{letter_msg}"
                            )
