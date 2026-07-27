def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)

    return -1

arr = list(map(int, input("Enter sorted array elements: ").split()))
key = int(input("Enter key: "))

result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print("Key found at index", result)
else:
    print("Key not found")
        
            
        
