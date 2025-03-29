# Create a program called dictionaries_transpose. The program should have a function named transpose_dictionary.
#  The function should take a dictionary as argument and transpose the dictionary so that it swaps the key and the value in each dictionary entry.
#  First, copy/paste the main function below to your program. Then write the transpose_dictionary  function.


def transpose_dictionary(my_dict):
    new_dict = {}
    for key, val in my_dict.items():
        new_dict[val] = key

    my_dict.clear()
    my_dict.update(new_dict)


def main():
    vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
    print(vocabulary)
    transpose_dictionary(vocabulary)
    print(vocabulary)


main()
