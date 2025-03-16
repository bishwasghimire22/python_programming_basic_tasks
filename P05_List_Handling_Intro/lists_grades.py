# Create a program called lists_grades that first inputs a grade letter from user. Then the program should compute and show the percentage of the grade letter found in a list that
#  contains the following values:  "A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"

grade_list = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
count_a = grade_list.count("A")
count_b = grade_list.count("B")
count_c = grade_list.count("C")

grade = input("Enter grade letter: ")

result = 0
if grade == "A":
    result = count_a / len(grade_list) * 100
if grade == "B":
    result = count_b / len(grade_list) * 100
if grade == "C":
    result = count_c / len(grade_list) * 100

print(f"{result:.1f} %")
"""
grade_list = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]

grade_input = input("Enter grade letter: ")
grade_count = grade_list.count(grade_input)
result = grade_count / len(grade_list) * 100

print(f"{result:.1f} %")
"""
