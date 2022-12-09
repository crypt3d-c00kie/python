#day 9
#grading program

'''
Grading System
91 - 100 : Outstanding
81 - 90 : Exceeds Expectation
71 - 80 : Acceptable
< 70 : Fail 
'''
def grade_this(given):

    student_grades = {}
    for student in given:
        if given[student] < 70:
            student_grades[student] = "Fail"
        elif given[student] >= 71 and given[student] <= 80:
            student_grades[student] = "Acceptable"
        elif given[student] >= 81 and given[student] <= 90:
            student_grades[student] = "Exceeds Expectation"
        elif given[student] >= 91:
            student_grades[student] = "Outstanding"

    print("Printing the Student_grades dict")
    print(student_grades)

def main():

    student_scores = {
        "Harry" : 81,
        "Ron" : 78,
        "Hermione" : 99,
        "Draco" : 74,
        "Neville" : 62
    }

    grade_this(student_scores)

main()