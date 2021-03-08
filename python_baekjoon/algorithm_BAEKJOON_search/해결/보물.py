n = int(input())
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))

a.sort()
b.sort(reverse=True)

x = 0
for i in range(n):
    x+=(a[i]*b[i])
print(x)


'''
[단계]
1. A를 오름차순으로 재배열한다.
2. B를 내림차순으로 재배열한다.
각 순서의 값을 서로 곱한다. 
'''