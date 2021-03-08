num = int(input())
a = 1
while(a<=num):
    if (a%3 == 0):
        print("X",end=" ")
    else:
        print(a,end=" ")
    a+=1