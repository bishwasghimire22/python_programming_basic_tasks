# Create a program called files_postcodes_1. The program should input a CSV file name from the user, read post-office data from a CSV file, input a postcode
#  from the user and print the post-office name in Finnish and Swedish as shown in the example output. The file postcodes.csv contains the post-office data to
#  be used in this exercise. Please download the file from the Moodle page. NB! When you open the file in a text editor, you can see the row structure.
#    INSTRUCTION   (To be carefully followed in this exercise)
#  The program should have a function called load_data that should
#   • Take a CSV file name as argument.
#  • Read the content of the CSV file using the Path class from the pathlib module
#  • Create a dictionary and save facts about each post-office to the dictionary
#  • Return a reference to the dictionary or return None if the CSV file is not found.
#  The main function should
#   • Input the name of the CSV file
#  • Call the load_data function
#  • Print the number of rows in the file, or "The file xxxx.yyy is not found"  if the file is not found (here xxxx.yyy is the inputted file name)
#  • If the file is found, input a postcode once and print facts about the post-office as shown in the example output, or "Unknown postcode"
#   if the postcode does not exist.
#  
from pathlib import Path


def load_data(data):
    my_dict = {}
    path = Path(data)
    contents = path.read_text(encoding="UTF-8")
    lines = contents.splitlines()

    for line in lines:
        fields = line.split(';')
        my_dict[fields[0]]= (fields[1], fields[2])
    return my_dict

def main():
    user_input = input("Enter postcode file name: ")
    try:
        data = load_data(user_input)
        if data:
            print(f"{len(data)} rows")
        else:
            print(f"The file {user_input} is not found")
        print()
        post_code = input("Enter postcode: ")
        if post_code in data:
            city, location = data[post_code]
            print(f"{post_code} {city}")
            print(f"{post_code} {location}")
        else:
            print("Unknown postcode")
        

    except FileNotFoundError:
         print(f"The file {user_input} is not found")
main()