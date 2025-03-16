# Create a program called lists_second. The program should first input words from the user until the user decides to quit by
#  entering "quit". Then the program should print the words in alphabetical order.
# You can suppose that the user writes all words in lowercase.

my_list = []
user_input = input("Enter a word (quit ends): ")

while user_input != "quit":
    my_list.append(user_input)
    user_input = input("Enter a word (quit ends): ")
my_list.sort()
print(my_list)
