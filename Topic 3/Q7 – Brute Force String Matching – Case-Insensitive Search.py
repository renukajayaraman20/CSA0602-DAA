text = input("Enter text: ")
pattern = input("Enter pattern: ")

text = text.lower()
pattern = pattern.lower()

for i in range(len(text) - len(pattern) + 1):

    j = 0

    while j < len(pattern):

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        print("Pattern found at position", i)
        break

else:
    print("Pattern not found")
#OUTPUT#
Enter text: DataStructuresAndAlgorithms
Enter pattern: ALGORITHMS
Pattern found at position 17
