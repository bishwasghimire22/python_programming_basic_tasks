# Create a program called lists_reverse. The program should first ask the user how many integers the user will
# enter. Then the program should input the integers from the user.
# Finally, the program should print the integers in reverse order on a single line as shown in the example output.
my_list = []
count = int(input("How many integers? "))
for i in range(count):
    user_input = int(input("Enter an integer: "))
    my_list.append(user_input)
my_list.reverse()
print()
print(*my_list)
