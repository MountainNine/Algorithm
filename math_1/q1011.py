t = int(input())
for c in range(t):
    x, y = input().split()
    # 1,1 2,2 3,3 4,3 5,4 6,4 7,5 8,5 9,5 10,6 11,6 12,6, 13,7
    #1, 2, 3~4, 5~6, 7~9, 10~12, 13~16
    #1  2   3    4    5     6      7
    sub = int(y) - int(x) - 1 #4
    be = int(sub ** (1 / 2))  #2
    af = be + 1  #3
    st = (af ** 2 - be ** 2) / 2 + be**2 #6.5
    if be**2 < sub+1 < st:
        print(af**2 - be**2 - 1)
    else:
        print(af**2 - be**2)
