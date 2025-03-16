# Create a program called strings_of_pearls that first inputs strings from the user until he/she decides to quit by entering the text "quit".
# Then the program should count how many times the user enters the string "pearl".
# The program should test the entered sting in case-insensitive way.
# If the user does not enter anything else but "quit", the program should not print anything else but "Bye!".
list_users = []
user_input = input("Enter first string: ")
if user_input == "quit":
    print("Bye!")
else:
    while user_input.lower() != "quit":
        list_users.append(user_input)
        user_input = input("Enter next string: ")

    count = 0

    for str in list_users:
        if str.lower() == "pearl":
            count += 1

    print()
    print(f"{count} pearls")
    print("Bye!")
