def mergesort(arr):
     if(len(arr)>1):
         mid=len(arr)//2
         left=arr[:mid]
         right=arr[mid:]
         mergesort(left)
         mergesort(right)
         i=j=k=0
         while(i<len(left) and j<len(right)):
             if left[i]<right[j]:
                 arr[k]=left[i]
                 i+=1
             else:
                 arr[k]=right[j]
                 j+=1
             k+=1
        while(j<len(right)):
                arr[k]=right[j]
                j+=1
                k+=1
arr=list(map(int,input("Enter array elements:").split()))
mergesort(arr)
print("Sorted array:",arr)
#--------------OUTPUT-------------#
Enter array elements: 38 27 43 3 9 82 10
Sorted array: [3, 9, 10, 27, 38, 43, 82]
Time Complexity: O(n log n)
