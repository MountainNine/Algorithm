t = int(input())

list_num = [False for x in range(10001)]
for i in range(10001):
    flag = True
    r = int(i ** (1 / 2))
    for j in range(2, r + 1):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        list_num[i] = True

for c in range(t):
    n = int(input())
    m = int(n / 2)
    while m > 0:
        if list_num[m] and list_num[n - m]:
            print("{} {}".format(m, n - m))
            break
        else:
            m -= 1
