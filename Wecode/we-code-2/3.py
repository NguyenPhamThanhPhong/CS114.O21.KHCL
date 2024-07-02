# from math import ceil, log10
import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
r, c = [int(num) for num in input().decode().split()]
a = []
for i in range(r):
    # inp = input().decode().split()
    # print(i.np)
    a += [input().decode().split()]
print(a)
t = []

t = [max((len(str(int(item)))) for item in column) for column in a]
for i in range(1, len(t)):
    t[i] += 1
print(t)
for i in range(r):
    s = ""
    for j in range(c):
        s += ("%" + str(t[j]) + "s") % ((a[i][j]))
    sys.stdout.write(s + "\n")
