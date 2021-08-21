# 10 20 25 15 10 20
# 10 20 35 10 10
n = int(input())
arr = [0 for x in range(n)]
for i in range(n):
    arr[i] = int(input())
cache = [0 for x in range(n)]
cache[0] = arr[0]
if n>=2:
    cache[1] = arr[0] + arr[1]
if n>=3:
    cache[2] = max(arr[0], arr[1]) + arr[2]
if n>=4:
    for i in range(3, n):
        cache[i] = max(cache[i - 2], cache[i - 3] + arr[i - 1]) + arr[i]
print(cache[n-1])
