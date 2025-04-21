# Create a program called functions_month_calendar. The program should have a function called print_month_calendar.
# The function should take year and month number as arguments and print a one-month calendar. See the example output below for more details.
#  The main function should first input year and month number from the user and then call the print_month_calendar function.

from datetime import date
from calendar import monthrange

month_names = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def print_month_calendar(year, month):
    my_date = date(year, month, 1)
    days_in_month = monthrange(my_date.year, my_date.month)[1]
    day_of_week = my_date.weekday() + 1

    print(f" > {month_names[month]} {year} <")
    print(" Mon Tue Wed Thu Fri Sat Sun")
    print("    "*(day_of_week-1), end="")

    for day in range(1, days_in_month + 1):
        print(f"{day:4d}", end= "")

        if (day_of_week + day -1) % 7 == 0:
            print()
            
    if (day_of_week + days_in_month - 1) % 7 != 0:
        print()

def main():
    input_year = int(input("Enter year: "))
    input_month = int(input("Enter month: "))
    print()
    print_month_calendar(input_year, input_month)

main()