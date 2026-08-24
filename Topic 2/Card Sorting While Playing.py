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
print("Time Complexity: O(n^2)")
print("Best Case: O(n)")
#----------OUTPUT----------#
Enter number of cards: 5
Enter card 1: 7
Enter card 2: 2
Enter card 3: 9
Enter card 4: 4
Enter card 5: 1
Sorted Hand: [1, 2, 4, 7, 9]
Time Complexity: O(n^2)
Best Case: O(n)
