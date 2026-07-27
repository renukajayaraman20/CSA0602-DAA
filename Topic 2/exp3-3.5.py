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
