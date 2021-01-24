prices = [1, 2, 3, 2, 3]
'''
return = [4,3,1,1,0]
다른 해법 : 최초로 더 낮은 값이 있는 경우, 인덱스 값 끼리 빼기
'''
answer = []

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] > prices[j]:
            seconds = j - i
            answer.append(seconds)
            break
        if j == len(prices)-1:
            seconds = j - i
            answer.append(seconds)
answer.append(0)

print(answer)
