summ = 0
txt = input().split(" ")
for i in txt:
    summ += int(i) ** 2

print(summ % 10)
