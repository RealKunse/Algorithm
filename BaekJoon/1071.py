num = int(input())
array = sorted(list(map(int, input().split())))
length = len(array)

ans_array = []
condition = True
before = array[0]

# print(array.remove(2))
print(array)
while condition:
    if len(ans_array) == length:
        condition = False

    print(ans_array)
    for i in range(len(array)):
        if array[i] != before + 1:
            before = array[i]
            ans_array.append(array.pop(i))
            break


print(ans_array)