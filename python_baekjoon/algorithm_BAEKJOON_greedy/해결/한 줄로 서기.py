'''
*항상 기준점을 잡고 시작한다.
4
2 1 1 0
---
4 2 1 3
(1) (2) (3) (4)
 2   1   1   0

(4) (2) (1) (3)     

1) 1번(가장 작은 사람)의 위치는 정해진다.
 - 자기보다 큰 사람이 왼쪽에 두 명, 즉 세 번째 자리
 _ _ 1 _

2) 2번(두 번째로 작은 사람)은 자기보다 큰 사람이 왼쪽에 한 명
  - 두 번째 위치
  일단 빈자리 1개

3) 3번은 자기보다 큰 사람이 왼쪽에 1개
 - 빈자리 1개 
'
'''


n = int(input())
# 4
lists = [0 for i in range(n)]
h = list(map(int,input().split(" ")))
# [2,1,1,0]
lists[h[0]] = 1 # [0,0,1,0]
for i in range(1,n): #i번째 순서 사람
    x = 0
    for j in range(n): #j번째 위치 자리
        if h[i] == x:
            if lists[j] == 0:
                lists[j] = i+1
                break
        elif lists[j]==0:
            x+=1
for i in lists:
    print(i,end=" ")
# 4 2 1 3 
