import math

mn, mx = list(map(int, [input(), input()]))

array = [True] * mx


def isPrimeNumber(num):
    for j in range(2, num + 1):
        print(j)
        if num % j == 0:
            return True

    return False


for i in range(0, len(array)):
    if isPrimeNumber(i):
        array[i] = i

print(isPrimeNumber(8))
print(array)