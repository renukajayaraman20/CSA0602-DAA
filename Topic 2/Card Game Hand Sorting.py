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
print("Time Complexity: O(n^2)")
print("Best Case: O(n)")
#------------OUTPUT-----------#
Enter number of cards: 7
Enter card 1: 2
Enter card 2: 4
Enter card 3: 6
Enter card 4: 8
Enter card 5: 9
Enter card 6: 11
Enter card 7: 13
Enter new card: 7
Sorted Hand: [2, 4, 6, 7, 8, 9, 11, 13]
Number of Passes: 5
