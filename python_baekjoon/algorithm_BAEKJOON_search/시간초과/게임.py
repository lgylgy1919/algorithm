'''
pypy3로 틀렸다고 나옴.
'''
x, y = map(int,input().split(" "))
z= int((y/x) * 100)

n = 0
if z == 99:
    print("-1")
else:
    while True:
        n+=1
        y+=1
        x+=1
        new_z = int((y/x) * 100) 
        if new_z != z:
            print(n)
            break

'''
게임 기록은 다음과 같이 생겼다.
게임 횟수 : X
이긴 게임 : Y (Z %)
Z는 형택이의 승률이다. 소수점은 버린다. 
예를 들어, X=53, Y=47이라면, Z = 88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 몇 판 더해야 
Z가 변하는지 구하는 프로그램을 작성하시오.

각 줄에 X와 Y가 주어진다. 
X는 1,000,000,000보다 작거나 같은 자연수이고, 
Y는 0보다 크거나 같고, X보다 작거나 같은 자연수이다.

첫째 줄에 형택이가 게임을 몇 판 해야하는지 출력한다. 
만약 Z가 절대 변하지 않는다면 -1을 출력한다.
'''