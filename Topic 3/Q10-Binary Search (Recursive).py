n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

m = int(input("Enter number of search keys: "))

for k in range(m):
    key = int(input("Enter search key: "))

    comparisons = 0
    found = False

    print("Comparisons:")

    for i in range(n):
        comparisons += 1
        print(arr[i], "==", key)

        if arr[i] == key:
            print("Element found at position", i + 1)
            found = True
            break

    if not found:
        print("Element not found")

    print("Total Comparisons =", comparisons)

print("\nBest Case Complexity : O(1)")
print("Average Case Complexity : O(n)")
print("Worst Case Complexity : O(n)")
print("Space Complexity : O(1)")

#---------------OUTPUT-------------#
Key found at index 3
Best Case: O(1)
Worst Case: O(log n)
Average Case: O(log n)
