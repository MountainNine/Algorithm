# 1 3 6 10 15
# 1 4 10 20 35
# 1 5 15 35 70
# 1 6 21 56 126

t = int(input())
for i in range(0, t):
    k = int(input())
    n = int(input())
    result = 0
    list_floor = list(range(1,n+1))
    for j in range(1,k+1):
        result = 0
        list_temp = []
        for k in range(0,n):
            result += list_floor[k]
            list_temp.append(result)
        list_floor = list_temp

    print(result)

