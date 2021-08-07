n = int(input())
list_n = []
for i in range(666,5000000):
    str_i = str(i)
    if '666' in str_i:
        list_n.append(i)

print(list_n[n-1])

# 1: 666
# 2~6: 0666~99666
# 7~16: 66600~66699
# 17~25: 16660~96669
# 26~35:
# 66600~66699
# 17666