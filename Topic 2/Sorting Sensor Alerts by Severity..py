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
#-----------OUTPUT------------#
Enter number of alerts: 10
Enter severity of alert 1: 2 
Enter severity of alert 2: 5
Enter severity of alert 3: 1
Enter severity of alert 4: 4
Enter severity of alert 5: 7
Enter severity of alert 6: 6
Enter severity of alert 7: 1
Enter severity of alert 8: 2
Enter severity of alert 9: 8
Enter severity of alert 10: 6
Sorted Alerts: [1, 1, 2, 2, 4, 5, 6, 6, 7, 8]
Plain Comparisons: 45
Optimized Comparisons: 39
