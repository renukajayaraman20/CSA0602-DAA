def max_crossing(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0

    for i in range(mid, low - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0

    for i in range(mid + 1, high + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_subarray(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    return max(
        max_subarray(arr, low, mid),
        max_subarray(arr, mid + 1, high),
        max_crossing(arr, low, mid, high)
    )


arr = list(map(int, input("Enter array elements: ").split()))

print("Maximum Subarray Sum:", max_subarray(arr, 0, len(arr) - 1))
