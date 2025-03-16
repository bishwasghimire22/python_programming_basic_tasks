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
my_date = date(2021, 12, 1)
