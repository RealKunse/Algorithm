num = int(input())

score = list(map(int, input().split()))
max_score = max(score)

answer = 0
for i in score:
    answer += i / max_score * 100

answer /= len(score)
print(answer)

