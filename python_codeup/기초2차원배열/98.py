'''
5 5 ( h / w)
3 ( n )
2 0 1 1 (l d x y)
3 1 2 3
4 1 2 5

1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''

h, w = map(int, input().split(" "))
n = int(input())
table = [[0 for i in range(w)] for j in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split(" "))
    if d == 0:
        for i in range(l):
            table[x-1][y-1] = 1
            y += 1
    else:
        for i in range(l):
            table[x-1][y-1] = 1
            x += 1

for i in range(h):
    for j in range(w):
        if j != w-1:
            print(table[i][j],end=" ")
        else:
            print(table[i][j])