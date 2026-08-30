text = input("Enter text: ")
pattern = input("Enter pattern: ")

positions = []

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern):
        if text[i + j] != pattern[j]:
            break
        j += 1

    if j == len(pattern):
        positions.append(i)

print("Occurrences at positions:", positions)
