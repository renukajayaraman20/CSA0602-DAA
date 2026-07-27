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
