n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key to search: "))

comparisons = 0
found = False

for i in range(n):
    comparisons += 1
    if arr[i] == key:
        found = True
        print("Element found at position", i + 1)
        break

if not found:
    print("Element not found")

print("Number of comparisons =", comparisons)
#-----------OUTPUT----------#
Enter element 1: 45
Enter element 2: 87
Enter element 3: 98
Enter element 4: 45
Enter element 5: 12
Enter key to search: 12
Element found at position 5
Number of comparisons = 5
