table = []
for i in range(19):
    a = list(map(int,input().split(" ")))
    table.append(a)

count = int(input())
for i in range(count):
    x, y=map(int,input().split(" "))
    for i in range(19):
        if table[x-1][i] == 1:
            table[x-1][i] = 0
        else:
            table[x-1][i] = 1
    for i in range(19):
        if table[i][y-1] == 1:
            table[i][y-1] = 0
        else:
            table[i][y-1] = 1


for i in range(19):
    for j in range(19):
        if j != 18:
            print(table[i][j],end=" ")
        else:
            print(table[i][j])

