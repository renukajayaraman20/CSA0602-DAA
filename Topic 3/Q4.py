n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter key: "))

count = 0

print("Occurrences at positions:")

for i in range(n):
    if arr[i] == key:
        print(i + 1, end=" ")
        count += 1

print()
print("Total occurrences =", count)
