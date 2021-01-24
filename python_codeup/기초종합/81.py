a, b = input().split(" ")
n = int(a)
m = int(b)
c = 1
d = 1
while(c<=n):
    while(d<=m):
        print(c,d)
        d += 1
    c += 1
    d = 1