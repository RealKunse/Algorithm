a = int(input())
member = []
for i in range(a):
  member.append(int(input()))

b, c = map(int,input().split())

print(member)

if (b>c):
  big = b
  small = c
else:
  big = c
  small = b

count = 0

for i in member:
  temp = i
  while temp > 0:
    while temp - big > 0:
      temp -= big
      count += 1
    while temp > 0:
      temp -= small
      count += 1

print(count)