# Create a program called references_weekdays.  First, copy/paste the code below to your program.
# The program should print the names of the weekdays when two company branches are open.
# The second company branch is open on the same weekdays as the first company branch plus on one more weekday.
# The weekday names are already added to the lists in the code above.
#  Unfortunately, the program above does not print the weekday names as expected.
#  Please fix the error without adding more code lines to the program.

from copy import deepcopy

weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]

weekdays_2 = deepcopy(weekdays_1)  # duplicate the first list
weekdays_2[0] = "Branch 2"  # change the branch name in the second list
weekdays_2[1].insert(1, "Tuesday")  # insert one more weekday name

print(*weekdays_1)
print(*weekdays_2)
