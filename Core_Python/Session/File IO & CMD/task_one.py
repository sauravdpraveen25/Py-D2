import sys
import os

filename = sys.argv[1]
location = sys.argv[2]

filepath = os.path.join(location, filename)

n = int(input("Enter number of lines: "))

with open(filepath, "w") as file:

    for i in range(n):
        line = input("Enter line: ")
        file.write(line + "\n")

print("\nFile Content:")

with open(filepath, "r") as file:
    data = file.read()

print(data)

lines = data.splitlines()
words = data.split()

chars_with_space = len(data)
chars_without_space = len(data.replace(" ", "").replace("\n", ""))

print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Characters With Spaces:", chars_with_space)
print("Characters Without Spaces:", chars_without_space)