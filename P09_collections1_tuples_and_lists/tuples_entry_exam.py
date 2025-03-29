# Create a program called tuples_entry_exam.
#  The program should have a function named grade_exam that takes a list of applicants and the exam passing score as arguments.
#  In the list, applicant names and exam scores are contained in tuples.
#  The grade_exam function should return a new list of tuples that contains only those applicants' names and scores who have passed the entry exam.
#  First, copy/paste the main function below to your program. Then write the grade_exam function.


def grade_exam(my_list: list, passing_score: int):
    passed_list = []

    for name, score in my_list:
        if score >= passing_score:
            passed_list.append((name, score))
    return passed_list


def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]

    passed_applicants = grade_exam(applicants, 30)
    print("Entry exam passed")
    for name, points in passed_applicants:
        print(f"{name}, {points} points")


if __name__ == "__main__":
    main()
