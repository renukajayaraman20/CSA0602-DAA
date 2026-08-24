x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

result = 1

for i in range(n):
    result *= x

print("Power:", result)
#----------OUTPUT----------#
Enter base: 2
Enter exponent: 10
Power: 1024
