def find_cons(n):
    m = 0
    for i in range(n,-1,-1):
        list_num = list(map(int, list(str(i))))
        if i + sum(list_num) == n:
            m = i
    return m


n = int(input())
print(find_cons(n))