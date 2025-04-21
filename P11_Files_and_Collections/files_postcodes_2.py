# Create a program called files_postcodes_2. The program should input a CSV file name from the user and read post-office data from a CSV file. 
# Then the program should input a place name from the user and print the postcodes and post-office names in the same language as the user entered the place name.

#  INSTRUCTION (to be carefully followed in this exercise) 
# • You should use the same file (postcodes.csv) in this exercise as you used in the previous exercise. 
# • You should copy the load_file function from the previous exercise and use it in this exercise. 
# The main function should  
# • Print "The file postcodes.csv is not found" if the file is not found  
# • If the file is found, input a place name once and print postcodes and post-office names as shown in the example output, or "No post-office found"  
# if the place name is not found. 

from pathlib import Path

def load_data(data):
    my_dict = {}
    script_dir = Path(__file__).parent
    file_path = script_dir / data
    contents = file_path.read_text(encoding="UTF-8")
    lines = contents.splitlines()

    for line in lines:
        fields = line.split(';')
        my_dict[fields[0]]= (fields[1], fields[2])
    return my_dict

def main():

    filename = "postcodes.csv"
    try:
        file = load_data(filename)

    except FileNotFoundError:
        print(f"The file {filename} is not found")
        return

    user_input = input("Enter place name: ").upper()
    found = False

    for postcode, (finnish_name, swedish_name) in file.items():
        if user_input == finnish_name.upper():
            print(f"{postcode} {finnish_name}")
            found = True
            

        elif user_input == swedish_name.upper():
            print(f"{postcode} {swedish_name}")
            found = True
           
    if not found:
        print(f"No post office found")

main()