# The program should print two lists of songs.
# The second song list should contain the same songs as the first song list plus two other songs.
#  The songs are already added to the lists in the code above.
# Unfortunately, the program above does not print the song lists as expected.
#  Please fix the error without adding more code lines to the program.

playlist_1 = ["Levitating", "Hold me closer", "As it was"]
playlist_2 = playlist_1.copy()

playlist_2.append("Bad Habit")
playlist_2.append("Shivers")

print("Playlist 1: ", end="")
print(*playlist_1, sep=", ")

print("Playlist 2: ", end="")
print(*playlist_2, sep=", ")
