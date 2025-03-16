# Create a program called gender_ distribution that first 
# inputs the number female students and the number of male students
#  from the user. Then, 
# the program should calculate the percentage of female students and the percentage of male students.
#  The program should show the percentages with one decimal place. 
# Enter the number of female students: 600
# Enter the number of male students: 200

# Female: 75.0 %
# Male: 25.0 %

female_students = int(input("Enter the number of female students: "))
male_students = int(input("Enter the number of male students: "))

total_students = female_students + male_students

if total_students == 0:
    female_percent = 0.0
    male_percent = 0.0
else:
    female_percent = float(female_students/total_students * 100)
    male_percent = float(male_students/total_students * 100)

print()
print(f"Female: {female_percent:.1f} %")
print(f"Male: {male_percent:.1f} %")