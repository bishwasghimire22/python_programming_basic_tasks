# Create a program called dictionaries_team_5 Copy/paste the dictionary from the Dictionaries Team 1 exercise to this program.
# The program should print team members' roles as shown in the example output. Please notice that each role is printed only once.

my_team = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

team_roles = set(my_team.values())

for role in sorted(team_roles):
    print(role)
