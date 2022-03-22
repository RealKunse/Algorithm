import math

num = int(input())
answer = 0
for i in range(num):
    txt = list(map(int, input().split()))
    answer = int(math.factorial(txt[1]) /
                 (math.factorial(txt[1] - txt[0]) * math.factorial(txt[0])))
    print(answer)