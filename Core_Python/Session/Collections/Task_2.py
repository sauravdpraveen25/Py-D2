student = {}

n = int(input("Enter Number of Students: "))

for i in range(n):

    rollno = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student[rollno] = {
        'name': name,
        'marks': marks
    }

print("\nStudent Dictionary")
print(student)

print("\n1. Student Roll Numbers")
print("2. Student Names")
print("3. Student Marks")

choice = int(input("Enter Choice: "))

if choice == 1:

    print("\nRoll Numbers")

    for rollno in student:
        print(rollno)

elif choice == 2:

    print("\nStudent Names")

    for rollno in student:
        print(student[rollno]['name'])

elif choice == 3:

    print("\nStudent Marks")

    for rollno in student:
        print(student[rollno]['marks'])

else:
    print("Invalid Choice")