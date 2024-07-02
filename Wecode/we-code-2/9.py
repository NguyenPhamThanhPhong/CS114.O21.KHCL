n = int(input())
x, y = [], []
for i in range(n):
    row = [int(num) for num in input().split()]
    x.append(row[0])
    y.append(row[1])


def crossProduct(x1, x2, x3, y1, y2, y3):
    #det = |a| * |b| * sin(theta)
    # rẽ phải thì sin(theta) <0 vẽ kim đồng hồ là thấy (-45)
    return (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)


count = 0
for i in range(2, n):
    if crossProduct(x[i - 2], x[i - 1], x[i], y[i - 2], y[i - 1], y[i]) < 0:
        count += 1
print(count)
