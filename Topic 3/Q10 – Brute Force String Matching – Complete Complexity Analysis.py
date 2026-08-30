text = input("Enter text: ")
pattern = input("Enter pattern: ")

comparisons = 0
positions = []

print("\nShifting Process:")

for i in range(len(text) - len(pattern) + 1):

    print("\nShift", i)
    print("Text portion:", text[i:i + len(pattern)])
    print("Pattern     :", pattern)

    j = 0

    while j < len(pattern):

        comparisons += 1

        print("Comparing", text[i + j], "with", pattern[j])

        if text[i + j] != pattern[j]:
            print("Mismatch")
            break

        print("Match")
        j += 1

    if j == len(pattern):
        print("Pattern matched")
        positions.append(i)

print("\nPattern occurrences:", positions)
print("Total comparisons =", comparisons)

print("\nBest Case Complexity = O(n)")
print("Worst Case Complexity = O(n * m)")
print("Space Complexity = O(1)")
