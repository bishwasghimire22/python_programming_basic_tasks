# Create a program called lists_surnames. The program should input surnames from the user until the user enters "ok".
# Then the program should print distinct surnames in alphabetical order as shown in the example output.
# Please notice that we can use a set to remove duplicates.

my_list = []

surname = input("Enter a surname (ok ends): ")

while surname != "ok":
    my_list.append(surname)
    surname = input("Enter a surname (ok ends): ")

new_list = list(set(my_list))

new_list.sort()
print()
print(*new_list, sep=", ")
