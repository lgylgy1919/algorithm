n = 5
sum = 0
for i in range(1, n+1):
    if n % i == 0:
        sum += i
print(sum)

'''
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
'''
