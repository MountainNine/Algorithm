while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a > b and a > c:
        print("right" if pow(b,2) + pow(c,2) == pow(a,2) else "wrong")
    elif b > a and b > c:
        print("right" if pow(a,2) + pow(c,2) == pow(b,2) else "wrong")
    else:
        print("right" if pow(a, 2) + pow(b, 2) == pow(c, 2) else "wrong")