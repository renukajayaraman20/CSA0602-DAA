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
#OUTPUT#
nter text: ABCDABCABCDA
Enter pattern: ABCD
Alignment 1 : Match
Pattern occurrence position = 0
Alignment 2 : Mismatch
Alignment 3 : Mismatch
Alignment 4 : Mismatch
Alignment 5 : Mismatch
Alignment 6 : Mismatch
Alignment 7 : Mismatch
Alignment 8 : Match
Pattern occurrence position = 7
Alignment 9 : Mismatch
