def printEl(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] == 1:
            temp.append(i+1)
            # print(i+1, end=" ")
    # print()
    result.append(temp)


def find_perm(list_n, arr, m, count):
    if count == m:
        printEl(arr)
    else:
        for n in list_n:
            if arr[n - 1] == 1:
                continue
            arr[n - 1] = 1
            find_perm(list_n, arr, m, count + 1)
            arr[n - 1] = 0


n, m = map(int, input().split())
list_n = list(range(1, n + 1))
arr = [0 for x in list_n]
result = []
find_perm(list_n, arr, m, 0)
result = (set(list(map(tuple,result))))
result = sorted(result)
for i in result:
    for j in i:
        print(j, end=" ")
    print()