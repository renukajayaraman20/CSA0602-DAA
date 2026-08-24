n = int(input("Enter number of participants: "))

names = []
scores = []

for i in range(n):
    name = input(f"Enter name of participant {i+1}: ")
    score = int(input(f"Enter score of {name}: "))

    names.append(name)
    scores.append(score)

for i in range(n):
    max_idx = i

    for j in range(i + 1, n):
        if scores[j] > scores[max_idx]:
            max_idx = j

    if max_idx != i:
        names[i], names[max_idx] = names[max_idx], names[i]
        scores[i], scores[max_idx] = scores[max_idx], scores[i]

    print(f"Rank {i+1}: {names[i]} - {scores[i]}")

print("Time Complexity: O(n^2)")
#----------OUTPUT----------------#
Enter score of RAVI: 95
Enter name of participant 3: MEERA
Enter score of MEERA: 79
Enter name of participant 4: DEV
Enter score of DEV: 98
Rank 1: DEV - 98
Rank 2: RAVI - 95
Rank 3: ASHA - 88
Rank 4: MEERA - 79
Time Complexity: O(n^2)
