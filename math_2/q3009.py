fx, fy = map(int, input().split())
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
x, y = 0, 0

if fx == sx:
    x = tx
elif fx == tx:
    x = sx
else:
    x = fx

if fy == sy:
    y = ty
elif fy == ty:
    y = sy
else:
    y = fy

print("{} {}".format(x, y))
