# Create a program called sharing_apples that first inputs the number 
# of apples and the number of children. 
# Then, the program should compute how many apples there are per
#  child and how many leftover apples there will be. 
# That is, each child should get the same number of apples.  
# NB!  Please use an arithmetic operator (%) to determine the
#  number of leftover apples

apple_count = int(input("How many apples? "))
student_count = int(input("How many children? "))

print(f"\nEach child will get {apple_count//student_count} apples.")
print(f"There will be {apple_count%student_count} leftover apples.")