#  Create a program called dictionaries_team_4 Copy/paste the dictionary from the Dictionaries Team 1 exercise to this program.
#  The program should ask the user to enter name and role. If the name is not in the dictionary, the program should add the inputted data to the dictionary.
#  If the name is already in the dictionary, the program should update the team member's role with the inputted role.
#  The program should keep repeating these steps until the user enters "quit" when the program asks the user to enter a name.
#  Finally, the program should print the team members' names and roles as shown in the example output.

my_team = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

name = input("Enter name (quit ends): ")
while True:
    if name.lower() == "quit":
        break
    role = input("Enter role: ")
    my_team[name] = role

    print()
    name = input("Enter name (quit ends): ")

print()
for key, value in sorted(my_team.items()):
    print(f"{key:<7} {value}")
