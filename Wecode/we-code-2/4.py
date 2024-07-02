r, c = [int(num) for num in input().split()]
a = []

for i in range(r):
    a.append(list(map(int, input().split())))


def calc(i, j):
    hor = [0, 1, -1, 0]
    ver = [1, 0, 0, -1]
    temp = 4
    for k in range(4):
        if i + hor[k] < 0 or i + hor[k] >= r or j + ver[k] < 0 or j + ver[k] >= c:
            continue
        else:
            temp -= 1 if a[i + hor[k]][j + ver[k]] != 0 else 0
    return temp


ans = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == 0:
            continue
        ans += calc(i, j)
print(ans)
