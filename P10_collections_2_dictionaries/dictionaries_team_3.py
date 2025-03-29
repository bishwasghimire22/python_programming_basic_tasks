# Create a program called dictionaries_team_3. Copy/paste the dictionary from the Dictionaries Team 1 exercise to this program.
# The program should ask the user to enter a team member's name and print the team member's role in the team.
#  If the name is not in the dictionary, the program should print the name and "is not in the team".
# The program should be repeating these steps until the user enters "quit" when the program asks the user to enter a name.

my_team = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

while True:
    user_input = input("Enter name(quit ends): ")

    if user_input.lower() == "quit":
        break

    if user_input in my_team:
        print(f"{user_input} is a {my_team[user_input]}")
    else:
        print(f"{user_input} is not in the team")
