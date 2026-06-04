def wordwise_reverse(s):
    words = s.split()
    words.reverse()

    for word in words:
        print(word, end=" ")

sentence = input("Enter a sentence: ")
wordwise_reverse(sentence)





def interchange_characters(s):
    chars = list(s)

    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    print("".join(chars))