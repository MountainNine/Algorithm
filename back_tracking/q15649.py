def printEl(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def find_perm(list_n, arr, m):
    if len(arr) == m:
        printEl(arr)
    else:
        for n in list_n:
            if n in arr:
                continue
            arr.append(n)
            find_perm(list_n, arr, m)
            arr.remove(n)


n, m = map(int, input().split())
list_n = list(range(1, n + 1))
arr = []
find_perm(list_n, arr, m)
