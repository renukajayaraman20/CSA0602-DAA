n = int(input("Enter number of players: "))

board = []

for i in range(n):
    board.append(int(input(f"Enter score {i+1}: ")))

new_score = int(input("Enter updated score: "))

board.append(new_score)

for i in range(1, len(board)):
    key = board[i]
    j = i - 1

    while j >= 0 and board[j] < key:
        board[j + 1] = board[j]
        j -= 1

    board[j + 1] = key

print("Updated Leaderboard:", board)
print("Time Complexity: O(n^2)")
print("Best Case: O(n)")
#-----------OUTPUT---------#
Enter number of players: 5
Enter score 1: 980
Enter score 2: 847
Enter score 3: 754
Enter score 4: 854
Enter score 5: 500
Enter updated score: 820
Updated Leaderboard: [980, 854, 847, 820, 754, 500]
Time Complexity: O(n^2)
Best Case: O(n)
