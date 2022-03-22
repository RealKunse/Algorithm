a, b = map(str, input().split())

a_ = ''
b_ = ''
for i in range(2, -1, -1):
    a_ += a[i]
    b_ += b[i]

a_ = int(a_)
b_ = int(b_)

if a_ > b_:
    print(a_)
else:
    print(b_)