n = int(input("Enter number of register numbers: "))

reg = []
for i in range(n):
    reg.append(int(input(f"Enter register number {i+1}: ")))

key = int(input("Enter register number to search: "))

for i in range(n):
    if reg[i] == key:
        print("Register Number found at position", i + 1)
        break
else:
    print("Register Number not found")
