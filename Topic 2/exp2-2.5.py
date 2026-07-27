n = int(input("Enter number of cards: "))

hand = []
for i in range(n):
    hand.append(int(input(f"Enter card {i+1}: ")))

new_card = int(input("Enter new card: "))
hand.append(new_card)

passes = 0
size = len(hand)

for i in range(size - 1):
    swapped = False
    for j in range(size - 1 - i):
        if hand[j] > hand[j + 1]:
            hand[j], hand[j + 1] = hand[j + 1], hand[j]
            swapped = True
    passes += 1
    if not swapped:
        break

print("Sorted Hand:", hand)
print("Number of Passes:", passes)
