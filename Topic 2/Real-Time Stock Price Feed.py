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
#-----------OUTPUT----------#
Enter number of stock prices: 5
Enter price 1: 102.5
Enter price 2: 98.3
Enter price 3: 102.8
Enter price 4: 78.9
Enter price 5: 97.5
Sorted Prices: [78.9, 97.5, 98.3, 102.5, 102.8]
Minimum Price: 78.9
Maximum Price: 102.8
