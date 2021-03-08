import math
w,m,k = map(int,input().split(" "))
lists = []
for i in range(0,k+1):
    ws = w-i
    ms = m-(k-i)
    if (math.floor(ws/2) >= ms):
        s = ms
        lists.append(s)
    else:
        s = math.floor(ws/2)       
        lists.append(s)

print(max(lists))
