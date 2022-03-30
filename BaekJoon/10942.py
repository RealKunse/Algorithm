import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
dp = [[0 for i in range(n)] for i in range(n)]
r = []

for i in range(int(input())):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    # 1글자면 무조건 팰린드롬.
    if start == end:
        r.append(1)
        dp[start][end] = 1
        continue

    # 2글자일 경우 각각 같은 숫자면 통과.
    # 아래 코드가 없어도 통과되지만, 미약하게 시간복잡도가 향상된다.
    if end - start == 1 and p[start] == p[end]:
        r.append(1)
        dp[start][end] = 1
        continue

    # 이미 팰린드롬으로 판별한 경우 팰린드롬 처리
    if dp[start][end] != 0:
        r.append(1)
        continue