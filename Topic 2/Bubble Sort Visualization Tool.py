n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("Original Array:", arr)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After Pass", i + 1, ":", arr)
#------------output--------#
Enter number of elements: 5
Enter element 1: 5
Enter element 2: 1
Enter element 3: 4
Enter element 4: 5
Enter element 5: 6
Original Array: [5, 1, 4, 5, 6]
After Pass 1 : [1, 4, 5, 5, 6]
After Pass 2 : [1, 4, 5, 5, 6]
After Pass 3 : [1, 4, 5, 5, 6]
After Pass 4 : [1, 4, 5, 5, 6]
