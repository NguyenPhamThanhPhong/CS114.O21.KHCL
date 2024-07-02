import bisect 
# import os, io
# import sys

# Python code to demonstrate working
# of binary search in library

n = int(input())

seen = set()
arr=list()
for i in input().split():
    if i not in seen:
        seen.add(i)
        arr.append(int(i))

k,value = map(int, input().split())

if(value <= arr[0]):
    print(*arr[0:k])
    exit()
if(value >= arr[-1]):
    print(*arr[-k:])
    exit()

# đây là code xử lý khi value nằm giữa mảng < arr[-1] và > arr[0]
# arr là mảng input đã bị lọc duplicate và giữ nguyên order
# value là giá trị so sánh absolute
# k là số lượng số cần in ra

index = bisect.bisect_left(arr, value)

min_boundary = max(0, index - k-1)
max_boundary = min(len(arr), index + k+1)

arr = arr[min_boundary:max_boundary]
arr = sorted(arr,key=lambda x:abs(x-value))
print(*sorted(arr[:k]))
