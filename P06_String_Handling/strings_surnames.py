# Create a program called strings_surnames. The program should first ask the user how many surnames the user will enter.
# Then the program should input the surnames from the user.
#  Finally, the program should print distinct surnames as shown in the example output.

"""surname_list = []
distinct_list = []
new_list = []
num_of_surnames = int(input("How many surnames? "))
for _ in range(num_of_surnames):
    surname = input("Enter a surname: ")
    surname_list.append(surname)
for s in surname_list:
    if s.lower() not in [x.lower() for x in distinct_list]:
        distinct_list.append(s)

distinct_list.sort(key=str.lower)
for s in distinct_list:
    new_list.append(s.capitalize())
print()
print(*new_list)
 """
num_of_surnames = int(input("How many surnames? "))
seen = set()
surname_list = []
distinct_list = []
new_list = []

for _ in range(num_of_surnames):
    surname = input("Enter a surname: ")
    surname_list.append(surname)


for s in surname_list:
    if s.lower() not in seen:
        distinct_list.append(s)
        seen.add(s.lower())


distinct_list.sort(key=str.lower)
print()

for s in distinct_list:
    new_list.append(s.capitalize())

print(*new_list)
