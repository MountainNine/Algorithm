n = int(input())
arr = list(map(int, input().split()))
cache = [1 for x in range(n)]
sol = 1
for i in range(0,n):
    temp = arr[i]
    for j in range(i):
        value = arr[j]
        if temp > value:
            cache[i] = max(cache[i], cache[j] + 1)
    sol = max(sol, cache[i])
print(sol)
# 60 50 40 30 20 10
# 10 20 10 30 20 50 10
# 30 10 20 50 60 70