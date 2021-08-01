import math

t = int(input())
for c in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    count = 0

    d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 + r2 > d > abs(r1 - r2):
        print(2)
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    elif r1 + r2 < d or abs(r1 - r2) > d:
        print(0)
    # if x2-i + y2- 13-i == r2
