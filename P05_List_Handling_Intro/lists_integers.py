# Create a program called lists_integers that first inputs five integers from the user and saves them to a list.
# Then the program should print the integers in descending order on a single line.
num_list = []
for i in range(5):
    num = int(input("Enter an integer:"))
    num_list.append(num)
num_list.sort(reverse=True)
print()
print(*num_list, end=" ")
