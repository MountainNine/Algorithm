m, n = input().split()
m, n = int(m), int(n)

for i in range(m, n + 1):
    flag = True
    r = int(i ** (1 / 2))
    for j in range(2, r + 1):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        print(i)