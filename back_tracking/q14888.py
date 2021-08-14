ma = -99999999
mi = 99999999


def calculate(a, b, i):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        return int(a / b)


def dfs(i, list_cal, middle):
    global ma, mi

    if list_cal[0] == 0 and list_cal[1] == 0 and list_cal[2] == 0 and list_cal[3] == 0:
        ma = max(ma, middle)
        mi = min(mi, middle)

    for j in range(len(list_cal)):
        if list_cal[j] > 0:
            list_cal[j] -= 1
            temp = calculate(middle, list_n[i + 1], j)
            dfs(i + 1, list_cal, temp)
            list_cal[j] += 1



n = input()
list_n = list(map(int, input().split()))
list_cal = list(map(int, input().split()))
dfs(0, list_cal, list_n[0])
print(ma)
print(mi)
