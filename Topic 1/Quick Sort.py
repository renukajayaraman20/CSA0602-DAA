def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = list(map(int, input("Enter array elements: ").split()))

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)

print("Best Case Time Complexity: O(n log n)")
print("Average Case Time Complexity: O(n log n)")
print("Worst Case Time Complexity: O(n^2)")
#-------------OUTPUT-----------#
Enter array elements: 10 7 8 9 1 5
Sorted Array: [1, 5, 7, 8, 9, 10]
Best Case Time Complexity: O(n log n)
Average Case Time Complexity: O(n log n)
Worst Case Time Complexity: O(n^2)
