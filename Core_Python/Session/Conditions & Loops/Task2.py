num = int(input("Enter a number: "))

if num > 0:

    if num % 2 != 0:
        print("Result:", num + 10)

    else:
        print("Result:", num * 2.5)

else:

    if num % 2 != 0:
        print("Result:", num - 10)

    else:
        print("Result:", num / 2.5)