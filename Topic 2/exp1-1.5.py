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
