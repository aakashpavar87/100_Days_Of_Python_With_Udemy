import csv
month = 11
day = 23
with open("./Birthday Wisher Project/birthdays.csv") as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        if f"{month}" in row[3] and f"{day}" in row[4]:
            print(row)
