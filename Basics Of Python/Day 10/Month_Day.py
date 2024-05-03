def is_leap(year):
    if (year % 4 == 0) :
        if(year % 100 != 0) :
            if(year % 400 != 0) :
                # print(f"Entered year {year} is a leap year")
                return True
        else:
            # print(f"Entered year {year} is not a leap year")
            return False
    else:
        # print(f"Entered year {year} is not a leap year")
        return False
def days_in_month(year,month):
    '''This function is created for checking days in particular month. Doc String by Aakash'''
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]
year_in = int(input("Enter year : "))
month_in = int(input("Enter month : "))
days = days_in_month(year=year_in,month=month_in)
print(f"There are {days} days in month No: {month_in}")
    
