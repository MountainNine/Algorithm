def list_reverse(lst):
    temp = []
    for i in range(len(lst)-1,-1,-1):
        temp.append(lst[i])
    return temp

a, b = input().split()
list_a = list(a)
list_b = list(b)
list_a = list(map(lambda x : int(x), list_a))
list_b = list(map(lambda x : int(x), list_b))

list_a = list_reverse(list_a)
list_b = list_reverse(list_b)

if len(list_a) > len(list_b):
    for i in range(0, len(list_a) - len(list_b)):
        list_b.append(0)
else:
    for i in range(0, len(list_b) - len(list_a)):
        list_a.append(0)

result = []
for i in range(0,len(list_a)):
    result.append(list_a[i] + list_b[i])

for i in range(0,len(result)):
    if result[i] >= 10:
        if i == len(result)-1:
            result.append(1)
        else:
            result[i+1] += 1
        result[i] -= 10


str_result = ""
for i in range(len(result)-1, -1, -1):
    str_result += str(result[i])
print(str_result)