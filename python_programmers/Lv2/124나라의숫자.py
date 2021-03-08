n = 15
answer = []


def fun(s):
    q, r = divmod(s, 3)
    if r == 0:
        answer.append(4)
        s = (s-3)/3
    elif r == 1:
        answer.append(1)
        s = (s-1)/3
    else:
        answer.append(2)
        s = (s-2)/3

    if s//3 < 1:
        answer.append(int(s))
        return(answer)
    else:
        fun(s)


fun(n)
answer.reverse()
if 0 in answer:
    answer.remove(0)
print(answer)
print("".join(map(str, answer)))

'''
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))
'''
