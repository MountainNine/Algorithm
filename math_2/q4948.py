list_num = [False for i in range(0, 246913)]
list_quest = []
while 1:
    inp = int(input())
    if inp == 0:
        break
    else:
        list_quest.append(inp)

for i in range(0, 246913):
    flag = True
    r = int(i ** (1 / 2))
    for j in range(2, r + 1):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        list_num[i] = True

for i in list_quest:
    i2 = i * 2
    count = 0
    for j in range(i + 1, i2 + 1):
        if list_num[j]:
            count += 1
    print(count)