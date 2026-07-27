n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key: "))

arr.append(key)

i = 0
comparisons = 0

while arr[i] != key:
    comparisons += 1
    i += 1

if i == n:
    print("Element not found")
else:
    print("Element found at position", i + 1)

print("Comparison count =", comparisons + 1)
