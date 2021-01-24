'''
2016년 1월 1일은 금요일
a월 b일은 무슨 요일?
31 29 31 30 31 30 31 31 30 31 30 31
'''
a = 1
b = 5

months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
days = 0
for m in range(a-1):
    days += months[m]

days += b
number = days % 7
answer = weeks[number-1]
print(answer)
