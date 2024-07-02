import numpy as np
from collections import deque

# 2d array input
m, n = map(int, input().split())
max_axis = min(m, n) / 2
a = deque()
for i in range(m):
    a.append(tuple(map(int, input().split())))
a = np.array(a)
i = 3
left = a[-1 - i : -m - 1 + i : -1, i]
right = a[i + 1 : m - i, -1 - i]
top = a[i, i + 1 : n - i]
bot = a[-1 - i, -2 - i : -n + i : -1]
print(right)
spring_roll = np.concatenate((left, top, right, bot))
print(spring_roll)
spring_roll = np.roll(spring_roll, 1)
print(spring_roll)
# a[i + 1 : m - i, -1 - i] = spring_roll[i : m - i]  # left
print(spring_roll[0 : m - 2 * i])
print(spring_roll[m - 2 * i : m + n - 1 - 4 * i])
print(spring_roll[m + n - 1 - 4 * i : m + 2 * n - 1 - 6 * i])
print(spring_roll[m + 2 * n - 1 - 6 * i : 2 * m + 2 * n - 2 - 8 * i])
# a[i, i + 1 : n - i] = spring_roll[m - i : m + n - 1 - i]  # top
# a[i + 1 : m - i, -1 - i] = spring_roll[m + n - 1 - i : m + n + n - 2 - i]
# a[-1 - i, -2 - i : -n + i : -1] = spring_roll[m + n + n - 2 - i :]
# print(a)
