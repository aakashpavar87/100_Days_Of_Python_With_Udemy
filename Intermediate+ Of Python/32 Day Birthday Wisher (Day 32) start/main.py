# from smtplib import *
# First create connection Then starttls for encryption then login to your account
# And then send mail to Recipient email address
import random

my_mail = "aakashpavar87@gmail.com"
my_pass = "Aakash@87"
# with SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_mail, password=my_pass)
#     connection.sendmail(
#         from_addr=my_mail,
#         to_addrs="aakashyahoo@yahoo.com",
#         msg="Subject:Hello\n\nDemo for body of mail"
#     )

# import datetime as dt
#
# my_date = dt.datetime.now()
# year = my_date.year
# month = my_date.month
#
# dob = dt.datetime(year=2004, month=9, day=2, hour=11, minute=25, second=55)
# print(dob)


import datetime as dt
import smtplib as sm


rt_mail = "ratanlaldabgar@gmail.com"
with open("quotes.txt", mode="r") as file_data:
    data = file_data.readlines()
my_day = dt.datetime.now()
if my_day.weekday() == 2:
    mail_sender = sm.SMTP("smtp.gmail.com")
    mail_sender.starttls()
    mail_sender.login(user=my_mail, password=my_pass)
    mail_sender.sendmail(from_addr=my_mail, to_addrs=rt_mail,
                         msg=f"Subject:Motivational Quote\n\n{random.choice(data)}")
    mail_sender.close()
