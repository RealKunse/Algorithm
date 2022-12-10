num = int(input())
dic = {}
count = 0
for i in range(101):
    dic[i] = {}
    for j in range(101):
      dic[i][j] = 0


for i in range(num):
    a, b = list(map(int, input().split()))
    for j in range(a, a+10):
        for k in range(b, b+10):
            dic[j][k] += 1


for i in range(101):
    for j in range(101):
        if dic[i][j] != 0:
            count += 1

print(count)