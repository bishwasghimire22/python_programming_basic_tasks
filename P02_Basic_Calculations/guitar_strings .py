#Create a program called guitar_strings that calculates the total cost of guitar strings a 
# guitarist will use on a set of gigs. The program first inputs the total number of gigs the
#  guitarist will do (integer), the number of gigs the guitarist plays with the same set of 
# strings, and the price of set of guitar strings (float). Then, the program should compute 
# and print how many sets of guitar strings the guitarist will need and the total cost of 
# guitar strings with two decimal places. This time, we suppose that the guitarist must buy 
# new guitar strings if he is going to do any gigs. 

num_of_gigs = int(input("Number of gigs: "))
gigs_per_set = int(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))

sets_needed = num_of_gigs//gigs_per_set

if num_of_gigs % gigs_per_set != 0:
    sets_needed +=1

    
total_cost = price * sets_needed
print(f"The guitarist needs {sets_needed} new sets of guitar strings")
print(f"The total cost is {total_cost:.2f} euros")


