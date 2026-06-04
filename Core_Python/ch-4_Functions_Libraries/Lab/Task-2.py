def calculate(*lists):

    if len(lists) == 1:
        print(lists[0])

    elif len(lists) == 2:
        result = lists[0] + lists[1]

        print("Concatenated List:", result)
        print("Maximum:", max(result))
        print("Minimum:", min(result))

    elif len(lists) == 3:
        result = lists[0] + lists[1] + lists[2]

        print("Concatenated List:", result)
        print("Sum:", sum(result))

    else:
        result = [x for lst in lists for x in lst]

        print("Concatenated List:", result)

        squares = list(map(lambda x: x * x, result))
        print("Squares:", squares)

        odd_numbers = [x for x in result if x % 2 != 0]
        print("Odd Numbers:", odd_numbers)