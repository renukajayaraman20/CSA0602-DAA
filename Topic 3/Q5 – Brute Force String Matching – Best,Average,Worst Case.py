text = input("Enter text: ")
pattern = input("Enter pattern: ")

comparisons = 0
found = False

for i in range(len(text) - len(pattern) + 1):

    for j in range(len(pattern)):
        comparisons += 1

        if text[i + j] != pattern[j]:
            break

    else:
        found = True
        break

print("Number of comparisons =", comparisons)

if found and comparisons == len(pattern):
    print("Best Case")
elif found:
    print("Average Case")
else:
    print("Worst Case")
