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
print("Best Case Time Complexity: O(n)")
print("Worst Case Time Complexity: O(n^2)")

#-----------OUTPUT------------#
Enter number of roll numbers: 5
Enter roll number 1: 101
Enter roll number 2: 201   
Enter roll number 3: 450 
Enter roll number 4: 103
Enter roll number 5: 152
Sorted roll numbers: [101, 103, 152, 201, 450]
Number of passes taken: 3
Best Case Time Complexity: O(n)
Worst Case Time Complexity: O(n^2)
