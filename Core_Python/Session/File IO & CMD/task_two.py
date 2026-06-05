import os

filename = input("Enter filename: ")
location = input("Enter location: ")

demo_path = os.path.join(location, filename)
dummy_path = os.path.join(location, "dummy.txt")

n = int(input("Enter number of lines: "))

with open(demo_path, "w") as file:

    for i in range(n):
        line = input("Enter line: ")
        file.write(line + "\n")

with open(demo_path, "r") as file:
    lines = file.readlines()

print("\nContent of demo.txt")

for line in lines:
    print(line, end="")

with open(dummy_path, "w") as file:

    for line in reversed(lines):
        file.write(line)

print("\n\nLine-wise reverse written to dummy.txt")

old_word = input("\nEnter word to replace: ")
new_word = input("Enter replacement word: ")

with open(dummy_path, "r") as file:
    data = file.read()

data = data.replace(old_word, new_word)

with open(dummy_path, "w") as file:
    file.write(data)

print("\nUpdated Content of dummy.txt")

with open(dummy_path, "r") as file:
    print(file.read())