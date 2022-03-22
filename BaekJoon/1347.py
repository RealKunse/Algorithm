import pprint

length = int(input())
txt = input()


dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]  # [x,y]
status = 0  #
map = [[0, 0]]  # 0,0 부터 시작

for i in txt:
    dx_ = dx[status % 4]
    dy_ = dy[status % 4]

    if i == 'R':
        status += 1
    elif i == 'L':
        status -= 1
    elif i == 'F':
        last = map[len(map) - 1]
        map.append([last[0] + dx_, last[1] + dy_])

x_d = []
y_d = []

for x, y in map:
    x_d.append(x)
    y_d.append(y)

max_x = max(x_d) - min(x_d)
max_y = max(y_d) - min(y_d)

array = [['' for col in range(max_x)] for row in range(max_y)]
pprint.pprint(array)

