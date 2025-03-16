# Create a program called lists_info that inputs five integers from the user and saves them to a list. The program should print the following: the count of the values in the list,
# the smallest value, the largest value, and the sum of the values in the list.
#
# Hint: Please notice that you can compute the required results by using Python's built-in functions.

my_list = []
for i in range(5):
    num = int(input("Enter an integer: "))
    my_list.append(num)
print()
print(f"Count: {len(my_list)}")
print(f"min: {min(my_list)}")
print(f"max: {max(my_list)}")
print(f"sum: {sum(my_list)}")
