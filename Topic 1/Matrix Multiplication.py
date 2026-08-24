r1 = int(input("Enter no.of rows of Matrix A: "))
c1 = int(input("Enter no.of columns of Matrix A: "))

A = []

print("Enter Matrix A:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible.")
else:
    B = []

    print("Enter Matrix B:")
    for i in range(r2):
        row = list(map(int, input().split()))
        B.append(row)

    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result Matrix:")
    for row in result:
        print(row)

    print("Time Complexity: O(n^3)")
        #----------------OUTPUT-------------#
Enter no.of rows of Matrix A: 2
Enter no.of columns of Matrix A: 2
Enter Matrix A:
1 2
3 4
Enter rows of Matrix B: 2
Enter columns of Matrix B: 2
Enter Matrix B:
5 6 
7 8
Result Matrix:
[19, 22]
[43, 50]
Time Complexity: O(n^3)
