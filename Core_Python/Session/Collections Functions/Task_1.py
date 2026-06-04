data = input("Enter values separated by comma: ")

values = data.split(",")

int_list = []
str_list = []

for value in values:

    if value.isdigit():
        int_list.append(int(value))

    else:
        str_list.append(value)

print("Integer List:", int_list)
print("Minimum:", min(int_list))
print("Maximum:", max(int_list))

str_list.reverse()

print("String List (Reversed):", str_list)