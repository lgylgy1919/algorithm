s = "a B z"
n = 4
answer = []

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in s:
    if i.isalpha() and i.islower():
        answer.append(lower[(lower.index(i)+n) % len(lower)])

    elif i.isalpha() and i.isupper():
        answer.append(upper[(upper.index(i)+n) % len(upper)])

    else:
        answer.append(i)


print(''.join(answer))

'''
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''
