arr = 18
numbers = 0

for n in list(str(arr)):
    numbers += int(n)

print(arr % numbers == 0)


'''
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
'''
