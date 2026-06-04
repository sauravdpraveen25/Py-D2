# BaseException is the parent class of all child exception classes.


try:
    # actual source code
    a = [1, 2, 3, 4]

    print('Second Element : ', a[2])

    print('Fourth Element : ', a[4])

    print('Zero Element   : ', a[0])


except IndexError:
    # error handling source code
    # custom message
    print('Index Error Occured.')
    # custom logic

try:
    i = 1
    f = 3.0 ** i
    for i in range(100):
        print(i, f)
        f = f ** 2
except OverflowError:
    print("Overflow Error Occurred")

fh = object
try:
    fh = open("testfile", "r")
    try:
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print("Error: can\'t find file or read data")
except IOError:
    print("Error: can\'t find file or read data")
finally:
    print("File Close")
    fh.close()
try:
    fh = open("testfile1", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("File Close")
    fh.close()

"""
ValueError
ImportError
ArithmeticError
"""

'''
SyntaxErrors-IndentationErrors get raised when the file/code is parsed, not when that line of code is executed.
If the syntax is wrong at a single point in the code,
the parser can't continue so all code after that line is un-parseable.
'''
