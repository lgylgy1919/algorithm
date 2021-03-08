# 짝수 대문자, 홀수 소문자
s = "try hello world"
s = s.split(" ")


answer = []

for i in s:
    word = []
    for n in range(len(i)):
        if n % 2 == 0:
            word.append(i[n].upper())
        else:
            word.append(i[n].lower())
    answer.append(''.join(word))

print(' '.join(answer))


'''
def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
'''
'''
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''
