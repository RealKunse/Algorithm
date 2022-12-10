import copy

num, mult = map(int, input().split())

prime_list = list(map(int, input().split()))
prime_list.sort()

res = copy.deepcopy(prime_list)

for i in prime_list:
    for j in prime_list:
        res.append(i*j)

print(res)
res.sort()
print(res)

print(res[mult-1])