table= []
for i in range(10):
    row = list(map(int,input().split(" ")))
    table.append(row)

x = 1
y = 1
while True :
    if table[x][y] == 2:
        table[x][y] = 9
        break
    else:
        table[x][y] = 9
        if table[x][y+1] == 1:
            x+=1
            if table[x][y] == 1:
                break
            elif table[x][y] == 0:
                table[x][y] = 9
            elif table[x][y] == 2:
                table[x][y] = 9
                break
        elif table[x][y+1] == 0:
            table[x][y+1] = 9
            y+=1
        elif table[x][y+1] == 2:
            table[x][y+1]=9
            break

for i in range(10):
    for j in range(10):
        if j != 9:
            print(table[i][j],end=" ")
        else:
            print(table[i][j])
