'''
3 1 4 2 5
2 4 1 3 5

1 2 3 4 5
4 3 2 1 5
o o o o x
'''
from operator import itemgetter
case = int(input())
answer = []
for i in range(case):
    n = 1
    cand_num = int(input())
    score_l = []
    for i in range(cand_num):
        score = list(map(int,input().split(" ")))
        score_l.append(score)
    score_l.sort(key=itemgetter(0))
    
    for i in range(1,cand_num):
        d = []
        for j in range(i):
            d.append(score_l[j][1])
        if score_l[i][1]<min(d):
            n+=1
    answer.append(n)
for i in range(case):
    print(answer[i])