x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

result = 1

for i in range(n):
    result *= x

print("Power:", result)
