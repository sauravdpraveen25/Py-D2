rows = int(input("Enter Number of Rows: "))

print("\n1. Triangle of 1s")
print("2. Number Pattern")
print("3. Reverse Star Pattern")
print("4. Pyramid Pattern")
print("5. Diamond Pattern")

choice = int(input("\nEnter Choice: "))

# Pattern 1
if choice == 1:

    for i in range(1, rows + 1):
        print("1 " * i)

# Pattern 2
elif choice == 2:

    num = 1

    for i in range(1, rows + 1):

        for j in range(i):
            print(num, end=" ")
            num += 1

        print()

# Pattern 3
elif choice == 3:

    for i in range(rows, 0, -1):
        print("* " * i)

# Pattern 4
elif choice == 4:

    for i in range(1, rows + 1):

        print(" " * (rows - i), end="")
        print("* " * i)

# Pattern 5
elif choice == 5:

    # Upper Pyramid
    for i in range(1, rows + 1):

        print(" " * (rows - i), end="")
        print("* " * i)

    # Lower Pyramid
    for i in range(rows - 1, 0, -1):

        print(" " * (rows - i), end="")
        print("* " * i)

else:
    print("Invalid Choice")