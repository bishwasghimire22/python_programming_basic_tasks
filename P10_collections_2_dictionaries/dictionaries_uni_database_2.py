# Create a program called dictionaries_uni_database_2. Please follow the instruction below.
#  1.  Save a copy of dictionaries_uni_database_1.py as dictionaries_uni_database_2.py
#  2.  Replace the old main function with the code below.
# Do should not modify the new main function.
#  3.  Write the remove_course function. The function
#   • should remove a course from a degree program.
#   • should print "Unknown degree program: " and the degree program name if the degree program name does not exist in the dictionary.
#   • should print "Unknown course: " and the course name if the course does not exist in the degree program.
# When you run the program, it should print exactly what is shown in the example output below.


def insert_degree_program(my_dict: dict, degree: str):
    if degree in my_dict:
        print(f"{degree} is already in the database")
    else:
        my_dict[degree] = []


def insert_course(my_dict: dict, degree: str, course: tuple):
    if degree not in my_dict:
        print(f"Unknown degree program: {degree}")
    else:
        if course in my_dict[degree]:
            print(f"{course[0]} is already in the database")
        else:
            my_dict[degree].append(course)


def print_degree_program(my_dict: dict, degree: str):
    if degree not in my_dict:
        print(f"Unknown degree program: {degree}")
    else:
        courses = my_dict[degree]
        total_credit = sum(course[1] for course in courses)
        if len(courses) < 2:
            print(f"{degree} ({len(courses)} course)")
        else:
            print(f"{degree} ({len(courses)} courses)")
        for course in courses:
            print(f"  {course[0]}, {course[1]} credits")
        print(f"  Total credits: {total_credit}")


def remove_course(my_dict, degree, course_name):

    if degree not in my_dict:
        print(f"Unknown degree program: {degree}")
    else:
        courses = my_dict[degree]

        for course in courses:
            if course_name == course[0]:
                courses.remove(course)
            else:
                print(f"Unknown course: {course_name}")


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
    print()

    remove_course(db, "ITBBA", "Python Programming")
    print_degree_program(db, "ITBBA")
    print()
    # Testing error handling
    insert_degree_program(db, "ITBBA")
    insert_course(db, "ITBBA", ("Time Management", 3))

    print_degree_program(db, "LOBBY")
    remove_course(db, "COMPU", "Surfing")
    remove_course(db, "ITBBA", "Surfing")


main()
