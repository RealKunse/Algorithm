node = int(input())
a = list(map(int, input().split()))
remove_num = int(input())
remove_list = [remove_num]

for i in range(len(a)):
    if i in remove_list:
        remove_list.append(i)
        del a[i]


print(a)
print(remove_list)
