from itertools import combinations #조합 함수

n = int(input())
list_n = [list(map(int, input().split())) for x in range(n)]
member = [i for i in range(n)]
team = []

for t in list(combinations(member, n//2)):
    team.append(t)
mi = 100000
for i in range(len(team)//2):
    t = team[i]
    stat_a = 0
    for j in range(n//2):
        m = t[j]
        for k in t:
            stat_a += list_n[m][k]

    t = team[-i-1]
    stat_b = 0
    for j in range(n//2):
        m = t[j]
        for k in t:
            stat_b += list_n[m][k]

    mi = min(mi, abs(stat_a - stat_b))
print(mi)