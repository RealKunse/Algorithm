num = int(input())
array = sorted(list(map(int, input().split())))

idx = len(array)//2

if len(array) % 2 == 0:
    print(array[idx-1] * array[idx])
else:
    print(array[idx] * array[idx])

