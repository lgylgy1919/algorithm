'''
로직은 맞으나 시간초과 발생
'''
import math
# 높이 기준 한 줄씩 더해서 두 배 하기

w = 8
h = 12

# 한 칸 지날때 오른쪽 아래 꼭지점 위치 구하기
square = 0
for i in range(w):
    square += h - math.ceil((i+1)*(h/w))

print(square*2)
