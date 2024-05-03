import smtplib as sm
import pandas
import datetime as dt
import random
import pywhatkit

with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter:
    cur_letter = letter.readlines()


today = dt.datetime.today()
today_tup = (today.month, today.day)
# MY_MAIL = "aakashpavar87@gmail.com"
# MY_PASS = "cwdfzwgskdqvquwf"

dob_data = pandas.read_csv("birthdays.csv")
dob_month = dob_data.month.to_list()
dob_day = dob_data.day.to_list()

birthday_dict = {(row.month, row.day): row for (index, row) in dob_data.iterrows()}

print(birthday_dict[today_tup])
if today_tup in birthday_dict:
    # fr_mail = birthday_dict[today_tup]["email"]
    fr_name = birthday_dict[today_tup]["name"]
    cur_letter[0] = cur_letter[0].replace("[NAME]", fr_name)
    letter_msg = "".join(cur_letter)
    letter_msg = "Subject: Happy Birthday Wish\n\n" + letter_msg
    pywhatkit.sendwhatmsg_instantly(phone_no="+916351771513", message=f"{letter_msg}")

