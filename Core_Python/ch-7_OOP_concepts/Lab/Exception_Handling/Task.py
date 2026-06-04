try:
    a = int(input("Enter first number: "))

    try:
        b = int(input("Enter second number: "))
        print(a / b)

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except ValueError:
        print("Invalid second number")

    finally:
        print("Inner Finally")

except ValueError:
    print("Invalid first number")

finally:
    print("Outer Finally")


try:
    c = int(input("Enter third number: "))
    print(100 / c)

except ValueError:
    print("Invalid third number")

except ZeroDivisionError:
    print("Third number cannot be zero")

finally:
    print("Second Try Finally")