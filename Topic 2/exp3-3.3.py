n = int(input("Enter number of stock prices: "))

prices = []

for i in range(n):
    price = float(input(f"Enter price {i+1}: "))

    prices.append(price)

    j = len(prices) - 2

    while j >= 0 and prices[j] > price:
        prices[j + 1] = prices[j]
        j -= 1

    prices[j + 1] = price

print("Sorted Prices:", prices)
print("Minimum Price:", prices[0])
print("Maximum Price:", prices[-1])
