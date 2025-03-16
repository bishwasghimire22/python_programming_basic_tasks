# Create a program called lists_words_from_url. The program should first fetch a word list from the given URL and save the words to a list.
# This we can do with the code below1.

#   from urllib.request import urlopen
#  url = "https://www.mit.edu/~ecprice/wordlist.10000"
# word_list = urlopen(url).read().splitlines()

# Then the program should determine and display the count of the words in the list, the average word length (float, no decimal-part formatting),
#  and how many words there are of each length (the count of one-letter words, the count of two-letter words etc) as shown in the example output.
# You can suppose that the longest word contains 22 letters. We can use the len function to get the length of a word. To create counters for words of different lengths, we can create another
# list and initialise it with 23 zeros as below.
# counters = [0] * 23
# The word lengths are between 1 and 22.
# You can use the word length as the index and leave the first element in the counters list untouched. Your PC should be connected to the Internet when you are running this program on your own PC.


from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().splitlines()

total_words = len(word_list)
total_length = 0
for word in word_list:
    total_length += len(word)

average_length = total_length / total_words

print(f"{total_words} words")
print(f"The average word length is {average_length}")
counters = [0] * 23

for word in word_list:
    word_length = len(word)
    if word_length >= 1 and word_length <= 22:
        counters[word_length] += 1

print("Length Count")
for i in range(1, 23):

    print(f"{i:>6} {counters[i]:>5}")
