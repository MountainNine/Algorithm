n = int(input())
r = int(n ** (1 / 2))
result = []


def insu(n):
    for i in range(2, n + 1):
        if n == 1:
            return result
        if n % i == 0:
            result.append(i)
            return insu(int(n / i))


insu(n)
if n != 1:
    for i in result:
        print(i)
