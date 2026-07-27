n = int(input("Enter number of alerts: "))

alerts = []
for i in range(n):
    alerts.append(int(input(f"Enter severity of alert {i+1}: ")))

plain = alerts.copy()
optimized = alerts.copy()

plain_comparisons = 0
optimized_comparisons = 0

# Plain Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        plain_comparisons += 1
        if plain[j] > plain[j + 1]:
            plain[j], plain[j + 1] = plain[j + 1], plain[j]

# Optimized Bubble Sort
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        optimized_comparisons += 1
        if optimized[j] > optimized[j + 1]:
            optimized[j], optimized[j + 1] = optimized[j + 1], optimized[j]
            swapped = True
    if not swapped:
        break

print("Sorted Alerts:", optimized)
print("Plain Comparisons:", plain_comparisons)
print("Optimized Comparisons:", optimized_comparisons)
