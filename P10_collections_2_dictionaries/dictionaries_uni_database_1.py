# Create a program called dictionaries_uni_database_1. The program should save facts about degree programs and their courses in a dictionary.
#  The facts per each degree program include the following:
#  • degree program name (the key in the dictionary)
#  • courses, which the degree program provides (the value in the dictionary – another collection)
#  NB!  Here we need some planning. Please, think carefully what kinds of collections you want to use in your program.
#   First, copy/paste the main function below to your program.
#   You should not modify the main function.
#  Then write the other functions.

# The insert_degree_program function
#  • should print the degree program name and " is already in the database" if the degree program name already exists in the dictionary.
# The insert_course function
#  • should print "Unknown degree program: " and the degree program name if the degree program name does not exist in the dictionary.
#  • should print  the course name and " is already in the database" if the course already exists in the degree program.
#  When you run the program, it should print exactly what is shown in the example output below.


def insert_degree_program(my_dict: dict, degree: str):
    my_dict[degree] = []


def insert_course(my_dict: dict, degree: str, course: tuple):
    my_dict[degree].append(course)


def print_degree_program(my_dict: dict, degree: str):

    courses = my_dict[degree]
    total_credit = sum(course[1] for course in courses)

    print(f"{degree} ({len(courses)} courses)")
    for course in courses:
        print(f"  {course[0]}, {course[1]} credits")
    print(f"  Total credits: {total_credit}")


def main():
    db = {}
    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")

    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5))
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))

    print_degree_program(db, "ITBBA")
    print_degree_program(db, "EXPER")


main()
