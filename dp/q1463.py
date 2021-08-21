#0,1,1,2,3,2,3
n = int(input())
cache = [0 for x in range(1000001)]
for i in range(1,n+1):
    temp = i
    cache[i] = cache[i-1] + 1
    if temp % 2 == 0:
        cache[i] = min(cache[i],cache[int(i/2)]+1)
    if temp % 3 == 0:
        cache[i] = min(cache[i],cache[int(i/3)]+1)
    if temp == 1:
        cache[i] = 0
print(cache[n])