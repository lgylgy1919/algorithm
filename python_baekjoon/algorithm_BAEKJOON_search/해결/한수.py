n = int(input())
x = 0
for i in range(1,n+1):
    arr = list(str(i))
    if len(arr) <=2:
        x+=1
    else:
        d = int(arr[1])-int(arr[0])
        y = 0
        for k in range(1,len(arr)):
            if (int(arr[k])-int(arr[k-1])) == d:
                y+=1
        if y == (int(len(arr))-1):
            x+=1
            
print(x)
