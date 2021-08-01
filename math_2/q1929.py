m, n = input().split()
m, n = int(m), int(n)

result = []
list_num = list(range(m, n + 1))
r = int(n ** (1 / 2))
for i in range(m, n + 1):
    r = int(i ** (1 / 2))
    f = False
    for j in range(2, r + 1):
        if i % j == 0 and i != j:
            f = True
            break
        elif i % j == 0 and i == j:
            print(i)
    if not f and i != 1:
        print(i)
