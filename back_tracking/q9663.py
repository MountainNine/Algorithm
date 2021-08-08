def find_queen(arr, r, c):
    for i, j in arr:
        if i - r == 0 or j - c == 0:
            return True
        elif abs(i - r) == abs(j - c):
            return True
    return False


def put_queen(board, arr, count):
    global result
    if count == n:
        result += 1
    else:
        for c in range(len(board[0])):
            if board[count][c] == 1:
                continue
            elif find_queen(arr, count, c):
                continue

            board[count][c] = 1
            arr.append((count, c))
            put_queen(board, arr, count + 1)
            board[count][c] = 0
            arr.remove((count, c))


n = int(input())
board = [[0 for x in range(n)] for y in range(n)]
result = 0
put_queen(board, [], 0)
print(result)
