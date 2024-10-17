import calendar

def print_monthly_calendar():

    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    print(calendar.month(year, month))

print_monthly_calendar()
