a = input()

a = a.replace("XXXX", "AAAA").replace("XX", "BB")
try:
    a.index("X")
    print(-1)
except:
    print(a)


