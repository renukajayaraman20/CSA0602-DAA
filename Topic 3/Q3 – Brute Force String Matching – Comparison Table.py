text = input("Enter text: ")
pattern = input("Enter pattern: ")

for i in range(len(text) - len(pattern) + 1):

    comparisons = 0
    match = True

    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        result = "Match"
    else:
        result = "Mismatch"

    print("Shift =", i,
          "Comparisons =", comparisons,
          "Result =", result)
    #----------OUTPUT-------#
Enter text: MISSISSIPPI
Enter pattern: ISSI
Shift = 0 Comparisons = 1 Result = Mismatch
Shift = 1 Comparisons = 4 Result = Match
Shift = 2 Comparisons = 1 Result = Mismatch
Shift = 3 Comparisons = 1 Result = Mismatch
Shift = 4 Comparisons = 4 Result = Match
Shift = 5 Comparisons = 1 Result = Mismatch
Shift = 6 Comparisons = 1 Result = Mismatch
Shift = 7 Comparisons = 2 Result = Mismatch
