def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = int(input("Enter a number: "))

print("Factorial using Iterative Method:", factorial_iterative(n))
print("Factorial using Recursive Method:", factorial_recursive(n))

print("Iterative Time Complexity: O(n)")
print("Recursive Time Complexity: O(n)")
#--------OUTPUT------------#
Enter a number: 5
Factorial using Iterative Method: 120
Factorial using Recursive Method: 120
Iterative Time Complexity: O(n)
Recursive Time Complexity: O(n)
