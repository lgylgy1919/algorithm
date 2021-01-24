'''
바둑판: 19x19
5
1 1
2 2
3 3
4 4
5 5
'''
'''
a = [[10, 20, 30], [30, 40,50], [50, 60, 50]]
print(a[2] [1])
'''
# line = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# table = []
# for i in range(0,19):
#     table.append(line)
count = int(input())
table = [[0 for i in range(19)] for j in range(19)]

for i in range(count):
    x,y = map(int,input().split(" "))
    table[x-1] [y-1] = 1

for i in range(19):
    for j in range(19):
        if j != 18:
            print(table[i][j],end=" ")
        else:
            print(table[i][j])
