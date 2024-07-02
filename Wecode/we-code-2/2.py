from collections import deque

r,c = map(int,input().split())
matrix = deque()

for i in range(r):
    row = str(input())
    matrix.append(row)

while matrix:
    print(matrix.pop())
