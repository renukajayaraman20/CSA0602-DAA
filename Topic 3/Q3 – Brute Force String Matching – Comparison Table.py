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
