# Create a program called files_read. The program should first input the name of a text file from the user.
# Then the program should read the file content and print it as it is. No formatting needed here.
#  Please read the content of the text file using the Path class from the pathlib module If the file is not found,
#  the program should print "The file xxxx.yyy is not found" (here xxxx.yyy is the inputted file name).
#  You can download the file files_keywords.txt from the Moodle page and use it in this exercise when you are running your program.
#  Of course, you can test your program using any text file on your PC.

from pathlib import Path

user_input = input("Enter file name: ")
try:
    dir = Path(__file__).resolve().parent
    path = dir / user_input

    content = path.read_text(encoding="UTF-8")
    print(content)
except FileNotFoundError:
    print(f"The file {user_input} is not found.")
