
m = int(input())
n = int(input())

result = []
for i in range(m, n + 1):
    r = int(i ** (1 / 2))
    f = False
    for j in range(2, r + 1):
        if i % j == 0 and i != j:
            f = True
            break
        elif i % j == 0 and i == j:
            result.append(i)
    if not f and i != 1:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])
