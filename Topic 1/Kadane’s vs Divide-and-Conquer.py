arr = list(map(int, input("Enter array elements: ").split()))

max_current = arr[0]
max_global = arr[0]

for i in range(1, len(arr)):
    max_current = max(arr[i], max_current + arr[i])
    max_global = max(max_global, max_current)

print("Maximum Subarray Sum:", max_global)
#---------OUTPUT----------#
Enter array elements: -2 -3 4 -1 -2 1 5 -3
Maximum Subarray Sum: 7
