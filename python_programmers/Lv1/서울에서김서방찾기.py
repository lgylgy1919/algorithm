seoul = ["Jane", "Kim"]

num = seoul.index("Kim")
print(f"김서방은 {num}에 있다.")


'''
javascript = `김서방은 ${num}에 있다'
python = f"김서방은 {num}에 있다."

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

def solution(seoul):
    return ('김서방은 %d에 있다' %seoul.index('Kim'))
'''
