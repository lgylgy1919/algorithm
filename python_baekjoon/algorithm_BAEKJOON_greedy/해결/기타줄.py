'''
6set 최솟값, 낱개 최솟값을 구한다.
case1) 낱개로 여러개 샀을 때
case2) 세트로 최대한 여러개 사고 남은 줄을 낱개로 샀을 때 
case3) 세트로만 구매했을 경우
'''
n,b = map(int,input().split(" "))
store = []
for i in range(b):
    sets = list(map(int,input().split(" ")))
    store.append(sets)

# 6set 최솟값, 낱개 최솟값을 구하기
six_list = []
for i in range(b):
    x = store[i][0]
    six_list.append(x)
six_min = min(six_list)
one_list = []
for i in range(b):
    y = store[i][1]
    one_list.append(y)
one_min = min(one_list)
# case1
best1 = one_min*n
# case2
o,s=divmod(n,6)
best2 = six_min*o + one_min*s
# case3
best3  = six_min*(o+1)

print(min(best1,best2,best3))