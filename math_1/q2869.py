inp = input()
a, b, v = inp.split()
a, b, v = int(a), int(b), int(v)
if (v-a) % (a-b) == 0:
    print(int((v-a)/(a-b)+1))
else:
    print(int((v-a)/(a-b)+2))
