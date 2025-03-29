# Create a program called dictionaries_count_letters. The program should first fetch the content of a text from the given URL and save it as single a string.
# This we can do with the code below.
# from urllib.request import urlopen
# url = "https://www.mit.edu/~ecprice/wordlist.10000"
# content = urlopen(url).read().decode("UTF-8")
# Then the program should count the letters in the string and display the result as shown in the example output below.
#  In this exercise,
# • you should use a dictionary to hold the count of occurrences of each distinct letter in the string
# • you should count letters in a case-insensitive way
# • you should not display a letter if it does not appear in the string.

from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000"
content = urlopen(url).read().decode("UTF-8")

letter_count = {}

for char in content.lower():
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

for letter, count in sorted(letter_count.items()):
    print(f"{letter}: {count}")
