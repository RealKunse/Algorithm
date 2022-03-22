x, y, w, h = map(int, input().split())

hor = w - x
ver = h - y

if hor > x:
    hor = x

if ver > y:
    ver = y

print(min([hor,ver]))