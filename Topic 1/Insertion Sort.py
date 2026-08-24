arr = list(map(int, input("Enter array elements: ").split()))

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

print("Sorted Array:", arr)
#----------OUTPUT------------3
Enter array elements: 12 11 13 5 6
Sorted Array: [5, 6, 11, 12, 13]
Best Case Time Complexity: O(n)
Average Case Time Complexity: O(n^2)
Worst Case Time Complexity: O(n^2)
