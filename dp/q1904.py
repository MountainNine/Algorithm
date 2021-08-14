n = int(input())
cache = [-1 for x in range(1000001)]
cache[1] = 1
cache[2] = 2


def result(n):
    if n == 1:
        return cache[1]
    elif n == 2:
        return cache[2]
    else:
        for i in range(3,n+1):
            cache[i] = (cache[i-1] + cache[i-2]) % 15746
        return cache[n]


print(result(n) % 15746)
# 1 2 3 5 8
# 00001 00111 11001 10000 10011 11100 11111 00100
#
