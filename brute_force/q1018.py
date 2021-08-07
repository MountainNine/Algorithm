n, m = map(int, input().split())
list_board = []
for i in range(n):
    board_row = list(input())
    list_board.append(board_row)

final_count = 65
for i in range(n - 7):
    for j in range(m - 7):
        count = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0 and l % 2 == 0 and list_board[i+k][j+l] != 'W':
                    count += 1
                elif k % 2 == 0 and l % 2 == 1 and list_board[i+k][j+l] != 'B':
                    count += 1
                elif k % 2 == 1 and l % 2 == 0 and list_board[i+k][j+l] != 'B':
                    count += 1
                elif k % 2 == 1 and l % 2 == 1 and list_board[i+k][j+l] != 'W':
                    count += 1
        final_count = min(final_count, count)
        count = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0 and l % 2 == 0 and list_board[i+k][j+l] != 'B':
                    count += 1
                elif k % 2 == 0 and l % 2 == 1 and list_board[i+k][j+l] != 'W':
                    count += 1
                elif k % 2 == 1 and l % 2 == 0 and list_board[i+k][j+l] != 'W':
                    count += 1
                elif k % 2 == 1 and l % 2 == 1 and list_board[i+k][j+l] != 'B':
                    count += 1
        final_count = min(final_count, count)

print(final_count)

# 9 10
# BBBBBBBBBB
# BWWBWBWBWB
# BWBWBWBWBW
# BWWBWBWBWB
# BWBWBBBWBW
# BWWBWBWBWB
# BWBWBWBWBW
# BWWBWBWBWB
# BWBWBWBWBW
