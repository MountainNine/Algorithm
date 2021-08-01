inp = input()
x, y, w, h = map(int, inp.split())
result = -1

result = x if x < w - x else w - x
temp = y if y < h - y else h - y
result = result if result < temp else temp
print(result)
# 6 2 10 3
