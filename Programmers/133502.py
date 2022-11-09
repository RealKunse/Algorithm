def solution(ingredient):
    stack = []
    cnt = 0
    for i in ingredient:
        stack.append(i)
        l = len(stack)
        if stack[l - 4:l] == [1, 2, 3, 1]:
            cnt += 1
            del stack[l - 4:l]

    return cnt


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
