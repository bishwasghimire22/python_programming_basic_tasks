# Create a program called dictionaries_translator. The program should first input Finnish and English words from the user until the user enters "quit".
#  The program should save the inputted words to a dictionary. The words should be saved in lowercase.
#  Next, the program should input an English word from the user and print the corresponding Finnish word.
#  If the English word does not exist in the dictionary, the program should print "Unknown word".
#  The program should keep repeating these steps until the user enters "quit" when the program asks the user to enter an English word.

print("=== Creating a dictionary ===")
wordlist = {}

eng_word = input("Enter english word (quit ends): ").lower()

while True:
    if eng_word == "quit":
        break

    finn_word = input("Enter finnish word: ").lower()

    wordlist[eng_word] = finn_word

    eng_word = input("Enter english word (quit ends): ").lower()

print("\n=== Using a dictionary ===")

user_input = input("Enter english word (quit ends): ").lower()

while True:
    if user_input == "quit":
        break
    if user_input in wordlist:
        print(wordlist[user_input])
    else:
        print("Unknown word")
    print()
    user_input = input("Enter english word (quit ends): ").lower()
