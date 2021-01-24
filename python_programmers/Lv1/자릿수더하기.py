n = 123
sum = 0
# print(map(sum, lambda x: int(x), list(str(n)))

for i in list(str(n)):
    sum += int(i)
print(sum)

'''
def sum_digit(number):
    return sum([int(i) for i in str(number)])

def sum_digit(number):
    return sum(map(int,str(number)))
'''
