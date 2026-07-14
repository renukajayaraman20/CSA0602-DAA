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
