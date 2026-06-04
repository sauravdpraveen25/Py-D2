class StudentInfo:

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


class StudentMarks:

    def __init__(self, roll_no, mark1, mark2, mark3):
        self.roll_no = roll_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_grade(self):

        average = (self.mark1 + self.mark2 + self.mark3) / 3

        print("Average:", average)

        if average > 100:
            print("Grade: Invalid Marks")
        elif average >= 90:
            print("Grade: A")
        elif average >= 80:
            print("Grade: B")
        elif average >= 60:
            print("Grade: C")
        elif average >= 40:
            print("Grade: D")
        else:
            print("Grade: Fail")


class Main:

    def __init__(self):

        n = int(input("Enter Number of Students: "))

        for i in range(n):

            print(f"\nEnter Details for Student {i + 1}")

            roll_no = input("Enter Roll Number: ")
            name = input("Enter Name: ")

            mark1 = int(input("Enter Marks 1: "))
            mark2 = int(input("Enter Marks 2: "))
            mark3 = int(input("Enter Marks 3: "))

            info = StudentInfo(roll_no, name)
            marks = StudentMarks(roll_no, mark1, mark2, mark3)

            print("\nStudent Details")
            print("Roll No:", info.roll_no)
            print("Name:", info.name)

            marks.calculate_grade()


obj = Main()