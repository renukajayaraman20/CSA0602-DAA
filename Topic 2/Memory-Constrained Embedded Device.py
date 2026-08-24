n = int(input("Enter number of temperature readings: "))
arr = []
for i in range(n):
    val = float(input(f"Enter reading {i+1}: "))
    arr.append(val)

a = arr.copy()
swaps = 0

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        swaps += 1

print("Sorted readings:", a)
print("Total swaps performed:", swaps)
print("Maximum possible swaps (n-1):", n - 1)
#-------------OUTPUT------#
Enter number of temperature readings: 3
Enter reading 1: 23.5
Enter reading 2: 19.2
Enter reading 3: 25.1
Sorted readings: [19.2, 23.5, 25.1]
Total swaps performed: 1
Maximum possible swaps (n-1): 2
