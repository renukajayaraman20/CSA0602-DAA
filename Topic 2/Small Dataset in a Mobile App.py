import time

n = int(input("Enter number of recently viewed items: "))
prices = []
for i in range(n):
    val = int(input(f"Enter price of item {i+1}: "))
    prices.append(val)

start = time.perf_counter()

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if prices[j] < prices[min_idx]:
            min_idx = j
    if min_idx != i:
        prices[i], prices[min_idx] = prices[min_idx], prices[i]

end = time.perf_counter()

print("Sorted prices:", prices)
print(f"Time taken: {(end - start) * 1_000_000:.2f} microseconds")
#-----------OUTPUT-----------#
Enter price of item 1: 499
Enter price of item 2: 129
Enter price of item 3: 456
Enter price of item 4: 789
Enter price of item 5: 452
Enter price of item 6: 156
Enter price of item 7: 123
Enter price of item 8: 412
Sorted prices: [123, 129, 156, 412, 452, 456, 499, 789]
Time taken: 47.40 microseconds
