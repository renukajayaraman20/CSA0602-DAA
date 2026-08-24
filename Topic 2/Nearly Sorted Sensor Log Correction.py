n = int(input("Enter number of temperature readings: "))

log = []

for i in range(n):
    log.append(float(input(f"Enter reading {i+1}: ")))

shifts = 0

for i in range(1, n):
    key = log[i]
    j = i - 1

    while j >= 0 and log[j] > key:
        log[j + 1] = log[j]
        j -= 1
        shifts += 1

    log[j + 1] = key

print("Sorted Log:", log)
print("Total Shifts:", shifts)
#-----------OUTPUT----------#
Enter number of temperature readings: 6
Enter reading 1: 18.5
Enter reading 2: 18.9
Enter reading 3: 17.9
Enter reading 4: 19.2
Enter reading 5: 19.5
Enter reading 6: 18.5
Sorted Log: [17.9, 18.5, 18.5, 18.9, 19.2, 19.5]
Total Shifts: 5
