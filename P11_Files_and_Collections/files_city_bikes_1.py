# Create a program called files_city_bikes_1. The program should read city bike usage data from a CSV file and print basic statistics on the bike rides as
#  shown in the example output. The file city_bike_rides_2021-06-30.csv contains the city bike usage data to be used in this exercise.
#  Please download the file from the Moodle page. NB! When you open the file in a text editor, you can see the column headers on the first line of the file.
#  Hint:  For your local testing, you can make a copy of the file city_bike_rides_2021-06-30.csv and give it a shorter name
#  INSTRUCTION   (To be carefully followed in this exercise)
# The program should have the following three functions: main, load_file, show_statistics
#
# The load_file function should
#  • Take a CSV file name as argument.
#  • Read the content of the CSV file using the Path class from the pathlib module
#  • Create a list that contains all other lines but not the first line read from the CSV file
#  • Return a reference to the list or return None if the CSV file is not found.
# The show_statistics function should
#  • Take a reference to a list (that contains the bike ride data) as argument.
#  • Compute and display bike ride statistics as shown in the example output.
# The main function should
#  • Input the name of a CSV file from the user. If the file is not found, the program should print "The file xxxx.yyy is not found" (here xxxx.yyy is the inputted file name).
#  • Call the load_file function.
#  • Print "The file xxxx.yyy is not found" (here xxxx.yyy is the inputted file name) if the file is not found.
#  • If the file is found, call the show_statistics function.

from pathlib import Path


def load_file(file): # type: ignore
    path = Path(file)
    contents = path.read_text(encoding="UTF-8")
    lines = contents.splitlines()
    return lines[1:]

def show_statistics(data):
    bike_rides = 0
    total_distance = 0
    total_duration = 0

    for line in data:
        fields = line.split(',')
        distance = int(fields[6])
        duration = int(fields[7])

        bike_rides += 1
        total_distance+=distance
        total_duration += duration
    total_km = total_distance/ 1000
    avr_distance = total_km/bike_rides
    avr_minutes = (total_duration/bike_rides)/60

    print(f"{total_km:.0f} kilometers on {bike_rides} bike rides")
    print(f"Average distance: {avr_distance:.1f} kilometers")
    print(f"Average duration: {avr_minutes:.0f} minutes")

def main():
    file_name = input(f"Enter file name: ")
    print()
    try:
        data = load_file(file_name)
        show_statistics(data)
    except FileNotFoundError:
        print(f"The file {file_name} is not found")

main()

    






# path = Path("cb_rides.csv")
# contents = path.read_text(encoding="UTF-8")
# lines = contents.splitlines()

# print(lines[0])

# for line in lines:
#   fields = line.split(",")
# print(line[0])


# print(contents)
# print(lines)
