phone_number = "01033334444"
print("*"*(len(phone_number)-4)+(phone_number)[-4:])

'''
[정규식 활용]
import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)
'''
