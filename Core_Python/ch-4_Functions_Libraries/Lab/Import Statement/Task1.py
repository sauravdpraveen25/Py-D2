total_students = int(input("Enter number of students: "))

students = []

with open("studentInfo.txt", "w") as info_file, \
     open("studentMarks.txt", "w") as marks_file:

    for i in range(total_students):
        print(f"\nEnter details for Student {i + 1}")

        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks1 = int(input("Enter marks of Subject 1: "))
        marks2 = int(input("Enter marks of Subject 2: "))
        marks3 = int(input("Enter marks of Subject 3: "))

        average = (marks1 + marks2 + marks3) / 3

        students.append(f"{roll_no}-{name}-{average:.2f}\n")

        info_file.write(f"{roll_no}-{name}\n")
        marks_file.write(f"{roll_no}-{marks1}-{marks2}-{marks3}\n")

print("\nStudent Details:")
for student in students:
    print(student, end="")

print("\nStudent data saved successfully.")