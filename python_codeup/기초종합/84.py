x, y, z = input().split(" ")
r = int(x)
g = int(y)
b = int(z)

for l in range(0,r):
    for m in range(0,g):
        for n in range(0,b):
            print(l,m,n)
print(r*g*b)3 