# Create a program called tuples_swap. The program should first input seven integers from the user and save them in a list.
#  Then the program should swap each successive pair of elements in the list.
# Finally, the program should print the list as shown Please see the example output for more details.
#  NB!  You should use slicing when you swap a pair of elements.

my_list = []

for i in range(7):
    user_input = int(input("Enter an integer: "))
    my_list.append(user_input)
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
