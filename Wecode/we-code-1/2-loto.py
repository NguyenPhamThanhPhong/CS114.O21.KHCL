
arr = [list(map(int,input().split())) for i in range(3)]
"""
For each item in range(3)
    item = list( 
        map the comming return of input().split() to int
    )
"""

n = int(input())
para = [int(input()) for i in range(n)] # 

def isBingo(parameter):
    return (all( (item in para) for item in parameter))
#phong's note: 
#for each item in PARAMETER => "return (item in para)"
check = False
left_cross=list()
right_cross=list()

for i in range(3):
    row = arr[i]
    col = [arr[j][i] for j in range(3)]
    if(isBingo(row) or isBingo(col)):
        check=True
        break
    left_cross.append(arr[i][i])
    right_cross.append(arr[i][2-i])

if(isBingo(left_cross) or isBingo(right_cross)):
    check = True

if check:
    print('Yes')
else:
    print('No')
