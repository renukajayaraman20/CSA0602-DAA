n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key: "))

comparisons = 0
matches = 0
mismatches = 0

for i in range(n):
    comparisons += 1
    if arr[i] == key:
        matches += 1
    else:
        mismatches += 1

print("Total Comparisons =", comparisons)
print("Total Matches =", matches)
print("Total Mismatches =", mismatches)
