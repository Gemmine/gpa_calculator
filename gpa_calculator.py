print("========  THIS IS A SEMESTER GPA CALCULATOR =========")

name = input("Enter your name: ")
matriculation_number = input("Enter your matriculation number: ")
department = input("Enter your department: ")
num_of_main_courses = int(input("Enter the number of main courses you're offered (not electives): "))
print("----------------------------------"*2)
print()

TNU = 0
TCP = 0

count = 0
while num_of_main_courses > count:
    course_code = input("Enter course code for course {} : ".format(count+1))
    num_of_unit = int(input("Enter number of unit for {} : ".format(course_code)))
    score_or_grade = input("Enter the score or grade you had for {} : ".format(course_code))
    print()
    grade = ""
    score = 0
    grade_point = 0
    credit_point = 0

    if type(score_or_grade) == "str" and type(score_or_grade) != "int" and type(score_or_grade) != "float":
        grade += score_or_grade.lower()
    else:
        score += float(score_or_grade)

    if score >= 70 or grade == "a":
        grade_point += 5
    elif 60 <= score < 70 or grade == "b":
        grade_point += 4
    elif 50 <= score < 60 or grade == "c":
        grade_point += 3
    elif 45 <= score < 50 or grade == "d":
        grade_point += 2
    elif 40 <= score < 45 or grade == "e":
        grade_point += 1
    elif score < 40 or grade == "f":
        grade_point += 0

    credit_point = grade_point * num_of_unit
    TCP += credit_point
    TNU += num_of_unit

    count += 1

GP = TCP/TNU
GP = round(GP, 2)
greetings = ""
grade_description = ""

if 4.5 <= GP <= 5.0:
    greetings += "Excellent Job!"
    grade_description += "First Class Honors"
elif 3.5 <= GP < 4.5:
    greetings += "Very good job!"
    grade_description += "Second Class Upper Division"
elif 2.4 <= GP < 3.5:
    greetings += "Good job!"
    grade_description += "Second Class Lower Division"
elif 1.5 <= GP < 2.4:
    greetings += "Fair Job!"
    grade_description += "Third Class"
elif 1.0 <= GP < 1.5:
    greetings += "Bad job!"
    grade_description += "Pass Degree"
elif 0.0 <= GP < 1.0:
    greetings += "Very bad job!"
    grade_description += "Failure!!!!"

print('\n\n{},'
      '\nAt the end of this Semester alone,'
      '\n{} with the matriculation number {},'
      '\nfrom {},'
      '\nhas a total grade of {} and is in {}.'
      '\n{} again.'.format(greetings, name, matriculation_number, department, GP, grade_description, greetings))
