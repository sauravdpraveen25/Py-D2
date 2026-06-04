def calculate(*lists):

    result = []

    for lst in lists:
        result.extend(lst)

    if len(lists) == 1:
        print("List:", result)

    elif len(lists) == 2:
        print("Concatenated List:", result)
        print("Maximum:", max(result))
        print("Minimum:", min(result))

    elif len(lists) == 3:
        print("Concatenated List:", result)
        print("Sum:", sum(result))

    squares = list(map(lambda x: x * x, result))
    print("Squares:", squares)

    odd_numbers = [x for x in result if x % 2 != 0]
    print("Odd Numbers:", odd_numbers)


n = int(input("Enter number of lists: "))

all_lists = []

for i in range(n):

    size = int(input(f"Enter number of elements in List {i + 1}: "))

    lst = []

    for j in range(size):
        element = int(input(f"Enter element {j + 1}: "))
        lst.append(element)

    all_lists.append(lst)

calculate(*all_lists)