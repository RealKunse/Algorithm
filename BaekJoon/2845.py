member = input().split()
member = int(member[1]) * int(member[0])

article = input().split()
for i in article:
    print(int(i) - member, end=" ")
