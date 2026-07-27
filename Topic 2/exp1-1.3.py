n = int(input("Enter number of books: "))
books = []
for i in range(n):
    val = int(input(f"Enter Book ID {i+1}: "))
    books.append(val)

a = books.copy()
moves = 0

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        moves += 1

print("Reordered shelf:", a)
print("Total physical moves:", moves)
print("Maximum possible moves (n-1):", n - 1)
