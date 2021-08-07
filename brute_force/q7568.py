def find_tie(list_dungchi):
    for i in range(len(list_dungchi)):
        rank = 1
        for j in range(len(list_dungchi)):
            if i == j: continue

            if list_dungchi[i][0] < list_dungchi[j][0] and list_dungchi[i][1] < list_dungchi[j][1]:
                rank += 1
        print(rank)


n = int(input())
list_dungchi = []
for i in range(n):
    x, y = map(int, input().split())
    list_dungchi.append((x, y))

find_tie(list_dungchi)
