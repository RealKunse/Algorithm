answer = [1, 1, 2, 2, 2, 8]
array = input().split()

for i in range(len(answer)):
    print(answer[i] - int(array[i]), end=" ")

