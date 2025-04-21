# Create a program called files_city_bikes_2. The program is an extended version of the files_city_bikes_1 program. 
#  The files city_bike_rides_small.csv and city_bike_rides_2021-06-30.csv contain the city bike usage data to be used in this exercise.
#  Please download the files from the Moodle page. INSTRUCTION   (To be carefully followed in this exercise) In addition to the previous output, 
# the program should print the names of those bike stations who have the highest number of departures. The bike station names should be printed in ascending order. 
# You should extend your previous code by writing a function named show_max_departures. 
# The function should 
# • Take a reference to a list (that contains the bike ride data) as argument. 
# • Compute and print names of the bike station(s) who has/have the highest number of departures.
#  The bike station names should be printed in ascending order. The main function should call the show_max_departures function. 

from pathlib import Path


def load_file(file):
    src_dir = Path(__file__).parent
    path = src_dir / file
    contents = path.read_text(encoding="UTF-8")
    return contents.splitlines()
    

def show_statistics(data):
    bike_rides = 0
    total_distance = 0
    total_duration = 0


    header = data[0].split(",")

    distance_idx = header.index("Covered distance (m)")
    duration_idx = header.index("Duration (sec.)")


    for line in data[1:]:
        fields = line.split(',')
        distance = int(fields[distance_idx])
        duration = int(fields[duration_idx])

        bike_rides += 1
        total_distance +=distance
        total_duration += duration
    total_km = total_distance/ 1000
    avr_distance = total_km/bike_rides
    avr_minutes = (total_duration/bike_rides)/60

    print(f"{total_km:.0f} kilometers on {bike_rides} bike rides")
    print(f"Average distance: {avr_distance:.1f} kilometers")
    print(f"Average duration: {avr_minutes:.0f} minutes")

def show_max_departures(data):
    header = data[0].split(",")
    station_idx = header.index("Departure station name")
    station_count = {}

    for line in data[1:]:
        fields = line.split(",")
        station_name = fields[station_idx]
        if station_name in station_count:
            station_count[station_name] += 1
        else:
            station_count[station_name] = 1

    max_departures = max(station_count.values())
    top_station = []
    for name, count in station_count.items():
        if count == max_departures:
            top_station.append(name)

    top_station.sort()
    print("Maximum number of departures from a bike station: ")
    for name in top_station:
        print(f"{name} ( {max_departures} departures)")



def main():
    file_name = input(f"Enter file name: ")
    print()
    try:
        data = load_file(file_name)
        show_statistics(data)
        print()
        show_max_departures(data)

    except FileNotFoundError:
        print(f"The file {file_name} is not found")

main()