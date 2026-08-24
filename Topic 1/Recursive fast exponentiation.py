def power(x, n):
    if n == 0:
        return 1

    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Power:", power(x, n))
#-------------OUTPUT-------------#
Enter base: 2
Enter exponent: 10
Power: 1024
