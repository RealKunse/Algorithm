def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for c in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % c == 0:
            return False  # 소수가 아님
    return True  # 소수임


a, b = map(int, input().split())

for i in range(a, b + 1):
    if is_prime_number(i):
        print(i)
