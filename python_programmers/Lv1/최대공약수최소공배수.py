n = 3
m = 12

answer = []
small = []
big = []

for i in range(1, min(n, m)+1):
    if n % i == 0 and m % i == 0:
        small.append(i)
answer.append(max(small))

for j in range(max(n, m), n*m + 1):
    if j % n == 0 and j % m == 0:
        big.append(j)
answer.append(min(big))


print(answer)
'''
[유클리드호제법??]
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
'''
'''
[]
def gcdlcm(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]
'''
