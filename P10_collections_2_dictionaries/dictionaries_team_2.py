# Create a program called dictionaries_team_2. Copy/paste the dictionary from the Dictionaries Team 1 exercise to this program.
# The program should print the team members as shown in the example output.

my_team = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

for key, value in my_team.items():
    print(key, end=" ")

print()

for key, value in sorted(my_team.items()):
    print(key, end=" ")
