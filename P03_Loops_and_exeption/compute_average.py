#Create a program called compute_average that first inputs decimal values from the user until 
# he/she decides to quit by entering zero. Then the program should compute and display the 
# average of the entered values (excluding the zero) with two decimals. If the only entered 
# value is zero, then the program should print "Nothing to be calculated". 
# Please notice the standard while loop pattern below and use it consistently to write clean code
# get first value
# while (...) 
# { process the value
# get next value
# } 
# NB! Please use the standard while loop pattern in this exercise.That is,
# 1.  Do not use the break statement. 
# 2.   Do not decrement a counter. 

num = float(input("Enter first number: "))
count = 0
total_sum = 0
#if num == 0:
    #print("Nothing to be calculated")
#else:
try:
    while num != 0:
        total_sum += num
        count += 1
        num = float(input("Enter next number: "))

    print(f"The average is {total_sum/count:.2f}")
except:
    print("Nothing to be calculated")