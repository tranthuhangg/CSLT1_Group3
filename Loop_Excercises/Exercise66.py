total_grade_points = 0
num_grades = 0

while True:
    grade = input("Enter a letter grade (blank to quit): ")
    if grade == "":
        break

    if grade == "A":
        grade_points = 4.0
    elif grade == "A-":
        grade_points = 3.7
    elif grade == "B+":
        grade_points = 3.3
    elif grade == "B":
        grade_points = 3.0
    elif grade == "B-":
        grade_points = 2.7
    elif grade == "C+":
        grade_points = 2.3
    elif grade == "C":
        grade_points = 2.0
    elif grade == "C-":
        grade_points = 1.7
    elif grade == "D+":
        grade_points = 1.3
    elif grade == "D":
        grade_points = 1.0
    elif grade == "F":
        grade_points = 0.0

    total_grade_points += grade_points
    num_grades += 1

if num_grades > 0:
    gpa = total_grade_points / num_grades
else:
    gpa = 0.0

print("The grade point average is:", gpa)