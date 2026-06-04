ls = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    ls.append(element)

total = sum(ls)

if total % 2 != 0:
    print("Equal division not possible")

else:
    half = total // 2
    running_sum = 0

    for i in range(len(ls)):
        running_sum += ls[i]

        if running_sum == half:

            ls1 = ls[:i + 1]
            ls2 = ls[i + 1:]

            print("List 1:", ls1)
            print("Sum:", sum(ls1))

            print("List 2:", ls2)
            print("Sum:", sum(ls2))

            break