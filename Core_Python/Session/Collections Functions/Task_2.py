student = {
    's1': {
        'rollno': None,
        'name': None,
        'marks': None,
        'grade': None
    },
    's2': {
        'rollno': None,
        'name': None,
        'marks': None,
        'grade': None
    },
    's3': {
        'rollno': None,
        'name': None,
        'marks': None,
        'grade': None
    },
    's4': {
        'rollno': None,
        'name': None,
        'marks': None,
        'grade': None
    },
    's5': {
        'rollno': None,
        'name': None,
        'marks': None,
        'grade': None
    }
}

for key in student:

    student[key]['rollno'] = input("Enter Roll No: ")
    student[key]['name'] = input("Enter Name: ")
    student[key]['marks'] = int(input("Enter Marks: "))

    marks = student[key]['marks']

    if marks >= 90:
        student[key]['grade'] = 'A'

    elif marks >= 80:
        student[key]['grade'] = 'B'

    elif marks >= 60:
        student[key]['grade'] = 'C'

    elif marks >= 40:
        student[key]['grade'] = 'D'

    else:
        student[key]['grade'] = 'Fail'

print("\nStudent Dictionary")

for key, value in student.items():
    print(key, ":", value)