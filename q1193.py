n = int(input())
i = 1
x, y = 0, 0
while n > i:
    n -= i
    i += 1

if i % 2 == 1:
    x = 1
    y = i
else:
    x = i
    y = 1

for j in range(1, n):
    if i % 2 == 1:
       x += 1
       y -= 1
    else :
        x -= 1
        y += 1

print(str(y) +"/" + str(x))