a, b, c = map(int, [input(), input(), input()])

txt = str(a * b * c)
array = []
for i in txt:
    array.append(i)

for i in range(0,10):
    print(array.count(str(i)))