def fibonacci_iterative(n):
    a, b = 0, 1
    print("Iterative Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# User Input
n = int(input("Enter the number of terms: "))
fibonacci_iterative(n)
print("Recursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
