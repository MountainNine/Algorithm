t = int(input())
for c in range(0, t):
    inp = input()
    h, w, n = inp.split()
    h, w, n = int(h), int(w), int(n)
    x = int(n / h) if n % h == 0 else int(n / h) + 1
    y = h if n % h == 0 else n % h
    print(str(y) + "0" + str(x) if x < 10 else str(y) + str(x))
