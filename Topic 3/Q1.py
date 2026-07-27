n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key to search: "))

comparisons = 0

for i in range(n):
    comparisons += 1
    if arr[i] == key:
        print("Element found at position", i + 1)
        print("Number of comparisons =", comparisons)
        break
else:
    print("Element not found")
