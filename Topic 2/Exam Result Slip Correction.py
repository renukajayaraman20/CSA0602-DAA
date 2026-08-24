n = int(input("Enter number of roll numbers: "))
rolls = []
for i in range(n):
    val = int(input(f"Enter roll number {i+1}: "))
    rolls.append(val)

passes = 0
for i in range(n - 1):
    passes += 1
    swapped = False
    for j in range(n - 1 - i):
        if rolls[j] > rolls[j + 1]:
            rolls[j], rolls[j + 1] = rolls[j + 1], rolls[j]
            swapped = True
    if not swapped:
        break

print("Sorted roll numbers:", rolls)
print("Number of passes taken:", passes)
#-----------OUTPUT------------#
Enter number of recently viewed items: 5
Enter price of item 1: 101
Enter price of item 2: 458
Enter price of item 3: 621
Enter price of item 4: 154
Enter price of item 5: 952
Sorted prices: [101, 154, 458, 621, 952]
Time taken: 27.70 microseconds
