import heapq
arr = list(map(int, input("Enter array elements: ").split()))
heapq.heapify(arr)
sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))
print("Sorted Array:", sorted_arr)
#-----------OUTPUT-----------#
Enter array elements: 4 10 3 5 1
Sorted Array: [1, 3, 4, 5, 10]
