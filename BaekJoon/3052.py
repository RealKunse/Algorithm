mod = {}
for i in range(0, 10):
    num = int(input()) % 42
    if num not in mod.keys():
        mod[num] = 1
    else:
        mod[num] += 1

print(len(mod))
