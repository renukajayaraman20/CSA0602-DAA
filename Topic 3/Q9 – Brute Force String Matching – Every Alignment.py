text = input("Enter text: ")
pattern = input("Enter pattern: ")

alignment = 1

for i in range(len(text) - len(pattern) + 1):

    j = 0

    while j < len(pattern):

        if text[i + j] != pattern[j]:
            break

        j += 1

    if j == len(pattern):
        print("Alignment", alignment, ": Match")
        print("Pattern occurrence position =", i)
    else:
        print("Alignment", alignment, ": Mismatch")

    alignment += 1
