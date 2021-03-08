s = "abcdef"
n = len(s)
lists = []
s = list(s)

if n % 2 == 0:
    lists.append(s[int(n/2-1)])
    lists.append(s[int(n/2)])
    answer = ''.join(lists)
else:
    answer = s[int((n-1)/2)]

print(answer)

'''
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]
'''
