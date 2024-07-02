p = []

for i in range(2):
    input_lst = list(input())
    if(input_lst[0]=="#"):
        p.append((0,i))
    if(input_lst[1]=="#"):
        p.append((1,i))

p_len = len(p)

if(p_len<2):
    print("No")
elif(p_len>2):
    print("Yes")
else:
    if(p[0][0]==p[1][0] or p[0][1]==p[1][1]):
        print("Yes")
    else:
        print("No")




