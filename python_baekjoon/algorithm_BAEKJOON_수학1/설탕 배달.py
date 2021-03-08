"""
- 주어진 값을 5로 나눈다. 몫을 구한다.
- 나머지를 3으로 나눠본다.
- 나누어 떨어지면 3으로 나눈 몫을 구한다.
- 나누어 떨어지지 않으면 처음에 5로 나눴을 때 구한 몫에 -1을 한다.
- 
divmod(x,y)  몫과 나머지
% 나머지
// 몫

"""
num = int(input())
a = num % 5  # (나머지)
b = num // 5  # (몫)
while True:
    if a % 3 == 0:
        print((num // 5) + (a // 3))
        break
    else:
        a += 5
        b -= 1
        num -= 5
        if b < 0:
            print(-1)
            break
