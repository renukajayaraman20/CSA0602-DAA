n = int(input("Enter number of participants: "))
scores = []
for i in range(n):
    val = int(input(f"Enter score {i+1}: "))
    scores.append(val)

k = int(input("Enter how many top scores you want: "))

arr = scores.copy()
k = min(k, n)

for i in range(k):
    max_idx = i
    for j in range(i + 1, n):
        if arr[j] > arr[max_idx]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]

print("Top", k, "scores:", arr[:k])
