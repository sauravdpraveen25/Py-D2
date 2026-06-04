def write_data(n):

    students = []

    with open("studentInfo.txt", "w") as info_file, \
         open("studentMarks.txt", "w") as marks_file:

        for i in range(n):

            print(f"\nStudent {i+1}")

            rollno = input("Enter Roll No: ")
            name = input("Enter Name: ")

            m1 = int(input("Enter Subject 1 Marks: "))
            m2 = int(input("Enter Subject 2 Marks: "))
            m3 = int(input("Enter Subject 3 Marks: "))

            info_file.write(f"{rollno}-{name}\n")
            marks_file.write(f"{rollno}-{m1}-{m2}-{m3}\n")

            average = (m1 + m2 + m3) / 3

            students.append(
                (rollno, name, average)
            )

    students.sort(
        key=lambda x: x[2],
        reverse=True
    )

    with open("Agrade.txt", "w") as a_file, \
         open("Bgrade.txt", "w") as b_file, \
         open("Cgrade.txt", "w") as c_file:

        for rollno, name, average in students:

            data = f"{rollno}-{name}-{average:.2f}\n"

            if average >= 80:
                a_file.write(data)

            elif average >= 60:
                b_file.write(data)

            elif average >= 40:
                c_file.write(data)


n = int(input("Enter Number of Students: "))

write_data(n)

print("\nData Stored Successfully")