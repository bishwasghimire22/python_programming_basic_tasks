# Create a program called tuples_clock. The program should have a function named roll_forward.
# The function should take the following as arguments:
#  • clock time as a tuple that contains hours (int) and minutes (int)
#  • the number of hours to be added to the clock time
#  • the number of minutes to be added to the clock time.
# The roll_forward function should roll the clock time forward and return a new clock time as a tuple.
# In the new clock time, hours should be between 0 and 23, and minutes should be between 0 and 59.
# The clock time should start from 00:00. The main function should
#  • input hours and minutes to be added to the clock time
#  • call the roll_forward function to roll the time forward
#  • print the new clock time. The program should terminate when the user enters negative hours.


def roll_forward(clock_time: tuple, add_hours: int, add_min: int):
    current_hour, current_min = clock_time
    total_minutes = current_min + add_min
    new_minutes = total_minutes % 60
    extra_hours = total_minutes // 60

    total_hours = current_hour + add_hours + extra_hours
    new_hour = total_hours % 24

    return new_hour, new_minutes


def main():
    clock_time = (0, 0)

    print("The current time is 00:00")
    while True:
        add_hour = int(input("Enter hours to add: "))
        if add_hour < 0:
            break
        add_minutes = int(input("Enter minutes to add: "))

        clock_time = roll_forward(clock_time, add_hour, add_minutes)

        print(f"{clock_time[0]:02}:{clock_time[1]:02}")


main()
