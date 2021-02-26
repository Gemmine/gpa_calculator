print('This is a GPA calcuator. Enter correct values please.')

name = input('What is your name? ')
mat_number = input('What is your matric number? ')
dept = input('What is the name of your department? ')
courses = int(input('How many main courses are you offering? '))
start = 0
count = 1

tcp = 0
tnu = 0
grade_point = 0

while courses > start:
    course_code = input(str(courses - (courses - count)) + '. What is your course code? ')
    unit = int(input('How many unit is ' + course_code + '? '))
    score = int(input('What did you score in ' + course_code + '? '))

    if score >= 70:
        grade_point = 5
    elif 60 <= score < 70:
        grade_point = 4
    elif 50 <= score < 60:
        grade_point = 3
    elif 45 <= score < 50:
        grade_point = 2
    elif 40 <= score < 45:
        grade_point = 1
    else:
        grade_point = 0

    tcp += (unit * grade_point)
    tnu += unit

    courses -= 1
    count += 1
else:
    gpa = round(tcp / tnu, 2)

if 4.5 <= gpa <= 5.00:
    greetings = 'Excellent job!'
    gpaDescription = 'First Class Honors'
elif 3.5 <= gpa < 4.5:
    greetings = 'Very good job!'
    gpaDescription = 'Second Class Upper Division'
elif 2.5 <= gpa < 3.5:
    greetings = 'Good job!'
    gpaDescription = 'Second Class Lower Division'
elif 1.5 <= gpa < 2.5:
    greetings = 'Fair job!'
    gpaDescription = 'Third Class'
elif 1.0 <= gpa < 1.5:
    greetings = 'Bad job!'
    gpaDescription = 'Pass Degree'
else:
    greetings = 'Very bad job!'
    gpaDescription = 'Failure!!!'

print('{0} At the end of the semester alone, {1} with matric number {2}, \nfrom {3} department '
      'has a total grade of {4} and is in {5}. \n'
      '{0} again.'.format(greetings, name, mat_number, dept, gpa, gpaDescription))

