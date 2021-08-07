# 3개의 수를 고른다
# 수의 합이 m을 넘지 않으면 sum에 저장
# m과 같다면 return sum
# m을 넘으면 break
from itertools import combinations


def find_card(list_card, list_sum, m):
    s = -1
    for i in list_sum:
        list_card_sum = []
        for j in i:
            list_card_sum.append(list_card[j])
        sum_list_card = sum(list_card_sum)
        if sum_list_card < m:
            s = max(s, sum_list_card)
        elif sum_list_card == m:
            return m
        else:
            continue

    return s


n, m = map(int, input().split())
list_card = list(map(int, input().split()))
range_n = list(range(n))
list_sum = list(combinations(range_n, 3))
print(find_card(list_card, list_sum, m))
