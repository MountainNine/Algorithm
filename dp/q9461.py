t = int(input())
cache = [-1 for x in range(101)]
cache[1] = 1
cache[2] = 1
cache[3] = 1

def result(n):
    if n in range(1,4):
        return cache[n]
    else:
        for i in range(4,n+1):
            cache[i] = (cache[i-2] + cache[i-3])
        return cache[n]

for i in range(t):
    n = int(input())
    print(result(n))
# 1 2 3 5 8
# 00001 00111 11001 10000 10011 11100 11111 00100
#
