a,b,c=map(int,input().split(" "))
d = 1
n = 1
while(d==1):
    if((n%a==0)&(n%b==0)&(n%c==0)):
        print(n)
        d =2
    else:
        n+=1

