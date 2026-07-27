n = int(input("Enter number of names: "))

names = []
for i in range(n):
    names.append(input(f"Enter name {i+1}: "))

key = input("Enter name to search: ")

for i in range(n):
    if names[i] == key:
        print("Name found at position", i + 1)
        break
else:
    print("Name not found")
