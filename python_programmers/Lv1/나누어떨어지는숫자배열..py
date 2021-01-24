arr = [3, 2, 6]
divisor = 10

answer = []
arr = sorted(arr)

for n in arr:
    if n % divisor == 0:
        answer.append(n)

if len(answer) >= 1:
    print(answer)
else:
    print(-1)

'''

def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''
