# Create a program called lists_unique_integers. The program should first input five integers.
#  Then the program should examine the inputted data and print the following:
#  distinct integer values in ascending order
#   all inputted values in ascending order.
my_list = []
for i in range(5):
    user_input = int(input("Enter an integer: "))
    my_list.append(user_input)

sorted_distinct = sorted(list(set(my_list)))
my_list.sort()

print(*sorted_distinct, sep=", ")
print(*my_list, sep=", ")
