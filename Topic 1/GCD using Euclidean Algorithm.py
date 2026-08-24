def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))
3-------------OUTPUT--------#
Enter first number: 48
Enter second number: 18
GCD = 6
