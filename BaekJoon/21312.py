a, b, c = map(int, input().split())

odd = 0
even = 0

even_list = []
odd_list = []

for i in [a, b, c]:
    if i % 2 == 0:
        even += 1
        even_list.append(i)
    else:
        odd += 1
        odd_list.append(i)

answer = 1

if odd >= 1:
    for i in odd_list:
        answer *= i
else:
    for i in even_list:
        answer *= i

print(answer)