n = int(input("Enter number of cards: "))

hand = []

for i in range(n):
    card = int(input(f"Enter card {i+1}: "))

    hand.append(card)

    j = len(hand) - 2

    while j >= 0 and hand[j] > card:
        hand[j + 1] = hand[j]
        j -= 1

    hand[j + 1] = card

print("Sorted Hand:", hand)
