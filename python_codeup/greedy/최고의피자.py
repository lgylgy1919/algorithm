'''
토핑 종류 수 : N
도우 가격, 토핑 가격 : A, B
도우 칼로리 : C
3+i~  토핑 칼로리 : Di

3(N)
12 2 (A, B)
200 (C)
50 (D1)
300 (D2)
100 (D3)
ans:37
'''
import math 
N = int(input())
A, B = map(int,input().split(" "))
C = int(input())
k = []
for i in range(N):
    d = int(input())
    k.append(d)
k.sort(reverse=True)

best = []

for i in range(N+1):
    price = A
    calorie = C
    for j in range(i):
        calorie += k[j]
        price += B
    v = calorie/price
    best.append(math.floor(v))

print(max(best))
