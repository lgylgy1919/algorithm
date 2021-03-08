n = 12345

n = list(str(n))
m = []
for i in n:
    m.append(int(i))

m.reverse()
print(m)

'''
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

'''
