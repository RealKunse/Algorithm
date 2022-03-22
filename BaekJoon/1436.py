n = 0

num = int(input())

for i in range(10000000):
    if '666' in str(i):
        n += 1
        if n == num:
            print(i)
            break

