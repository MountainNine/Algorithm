t = int(input())
cache = [(-1, -1) for x in range(41)]
cache[0] = (1, 0)
cache[1] = (0, 1)


def sum_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def fibonacci(n: int):
    if n == 0:
        return cache[0]
    elif n == 1:
        return cache[1]
    else:
        if cache[n-1] != (-1,-1) and cache[n-2] != (-1,-1):
            cache[n] = sum_tuple(cache[n-1] , cache[n-2])
        else:
            cache[n] = sum_tuple(fibonacci(n - 1) , fibonacci(n - 2))
    return cache[n]


for x in range(t):
    n = int(input())
    result = fibonacci(n)
    print(str.format("{} {}", result[0], result[1]))
