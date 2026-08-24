n=int(input("Enter the no. of elements in the array:"))
arr=[]
print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the key to search:"))
found=False
for i in range(len(arr)):
    if(arr[i]==key):
        print("Key found at index:",i)
        found=True
        break
if not found:
    print("Key not found")
#------------OUTPUT----------#
Enter the no. of elements in the array: 5
Enter the array elements:
10
25
30
45
50
Enter the key to search: 30
Key found at index: 2
Best Case Time Complexity: O(1)
Average Case Time Complexity: O(n)
Worst Case Time Complexity: O(n)
