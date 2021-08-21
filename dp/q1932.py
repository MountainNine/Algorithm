n = int(input())
arr = [[] for x in range(n)]
cache = [[0 for x in range(y+1)] for y in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

cache[0][0] = arr[0][0]

for i in range(1,n):
    for j in range(i+1):
        if 1<= j <= i-1:
            cache[i][j] = max(cache[i-1][j], cache[i-1][j-1]) + arr[i][j]
        elif j == 0:
            cache[i][j] = cache[i-1][j] + arr[i][j]
        else:
            cache[i][j] = cache[i-1][j-1] + arr[i][j]

print(max(cache[n-1]))