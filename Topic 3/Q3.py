n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key: "))

for i in range(n):
    if arr[i] == key:
        print("First occurrence at position", i + 1)
        break
else:
    print("Element not found")
