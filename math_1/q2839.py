n = int(input())
result = 0

if n % 5 == 0:
    result = int(n / 5)
else:
    f = int(n / 5)
    for i in range(f, -1, -1):
        r = n - i * 5
        if r % 3 == 0:
            result = i + int(r / 3)
            break
        result = -1

print(result)
