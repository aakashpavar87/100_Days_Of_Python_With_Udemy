import random
import smtplib as sm
from dbz import *

my_mail = "aakashpavar87@gmail.com"
my_pass = "cwdfzwgskdqvquwf"

fr_mail = "test.python590@gmail.com"
fr_pass = "emmzdocdgafjzlik"

# with sm.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_mail, password=my_pass)
#     connection.sendmail(from_addr=my_mail, to_addrs=fr_mail, msg="Subject:Hello\n\nTesting Python Code")
with open("quotes.txt", mode="r") as file:
    content = file.readlines()
with sm.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=fr_mail, password=fr_pass)
    connection.sendmail(from_addr=fr_mail,
                        to_addrs=my_mail,
                        msg=f"Subject:Hello\n\nTesting Python Code\n{vegeta}\n{random.choice(content)}"
                        )
