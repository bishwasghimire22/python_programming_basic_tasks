# Create a program called functions_earnings. The program should have a function called compute_earnings that
# takes hourly wage and hours worked as arguments. The function should compute and return the earnings.
# The overtime pay is time-and-a-half after 40 work hours. The main function should first input hourly
# wage and hours (integer) from the user and then call the compute_earnings function with the inputted values.
# Finally, the main function should print the earnings with two decimal places.
#
# NB! The compute_earnings function should not print anything.


def compute_earnings(hourly_wage: float, hours_worked: float):
    regular_hours = 40
    overtime_rate = 1.5

    if hours_worked > regular_hours:
        overtime_wage = hourly_wage * overtime_rate
        return (
            overtime_wage * (hours_worked - regular_hours) + hourly_wage * regular_hours
        )

    else:
        return hours_worked * hourly_wage


def main():
    hourly_wage = float(input("Enter wage: "))
    hours_worked = float(input("Enter hours: "))

    total_wage = compute_earnings(hourly_wage, hours_worked)
    print(f"The earnings are {total_wage:.2f}")


main()
