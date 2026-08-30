text = input("Enter text: ")
pattern = input("Enter pattern: ")

comparisons = 0

for i in range(len(text) - len(pattern) + 1):

    j = 0

    while j < len(pattern):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        print("First occurrence position =", i)
        print("Number of comparisons =", comparisons)
        break

else:
    print("Pattern not found")
    print("Number of comparisons =", comparisons)
#-OUTPUT----#
Enter text: COMPUTERSCIENCE
Enter pattern: SCI
First occurrence position = 8
Number of comparisons = 11
