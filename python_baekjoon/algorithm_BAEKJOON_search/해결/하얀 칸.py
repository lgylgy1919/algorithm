x=0
for i in range(1,9):
    lists = list(input())
    if i%2==1:
        for j in range(1,5):
            if lists[(2*j)-2] == "F":
                x+=1
    else:
        for k in range(1,5):
            if lists[(2*k)-1] =="F":
                x+=1

print(x)
