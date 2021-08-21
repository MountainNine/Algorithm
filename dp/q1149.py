n = int(input())
cache = [[0 for a in range(3)] for b in range(n+1)]
arr = [[0 for x in range(3)] for y in range(n+1)]
for i in range(1,n+1):
    arr[i] = list(map(int, input().split()))
for i in range(1,n+1):
    cache[i][0] = min(cache[i-1][1], cache[i-1][2]) + arr[i][0]
    cache[i][1] = min(cache[i-1][0], cache[i-1][2]) + arr[i][1]
    cache[i][2] = min(cache[i-1][1], cache[i-1][0]) + arr[i][2]

print(min(cache[n]))

