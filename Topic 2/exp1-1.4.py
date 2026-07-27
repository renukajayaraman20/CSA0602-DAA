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
    names[i], names[max_idx] = names[max_idx], names[i]
    scores[i], scores[max_idx] = scores[max_idx], scores[i]
    print(f"Rank {i+1}: {names[i]} - {scores[i]}")
