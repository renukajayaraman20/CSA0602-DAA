rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
    matrix.append(row)

key = int(input("Enter key: "))

found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)
            found = True
            break
    if found:
        break

if not found:
    print("Element not found")
