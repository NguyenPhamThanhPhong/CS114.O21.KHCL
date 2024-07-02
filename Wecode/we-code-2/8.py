import sys
n= int(input())
a=[None]*n
count = 0

for i in range(n):
    a[i] = sys.stdin.readline()
    if(i>=(n//2) and a[n-1-i] != a[i]):
        count+=1
    if count>1:
        print("FALSE")
        exit()
print("TRUE")
