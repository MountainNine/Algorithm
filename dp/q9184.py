cache = [[[-1 for x in range(101)] for y in range(101)] for z in range(101)]


def w(a, b, c):
    x, y, z = a + 50, b + 50, c + 50
    if a <= 0 or b <= 0 or c <= 0:
        cache[x][y][z] = 1
    elif a > 20 or b > 20 or c > 20:
        cache[x][y][z] = w(20, 20, 20)
    elif a < b < c:
        if cache[x][y][z - 1] != -1 and cache[x][y - 1][z - 1] != -1 and cache[x][y - 1][z] != -1:
            cache[x][y][z] = cache[x][y][z - 1] + cache[x][y - 1][z - 1] - cache[x][y - 1][z]
        else:
            cache[x][y][z] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        if cache[x - 1][y][z] != -1 and cache[x - 1][y - 1][z] != -1 and cache[x - 1][y - 1][z - 1] != -1 and \
                cache[x - 1][y][z - 1] != -1:
            cache[x][y][z] = cache[x - 1][y][z] + cache[x - 1][y - 1][z] + cache[x - 1][y][z - 1] - cache[x - 1][y - 1][
                z - 1]
        else:
            cache[x][y][z] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return cache[x][y][z]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a, b, c)
    print(str.format('w({}, {}, {}) = {}', a, b, c, result))
