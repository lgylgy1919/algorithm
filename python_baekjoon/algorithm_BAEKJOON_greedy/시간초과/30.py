numbers = list(map(int,list(input())))
l = len(numbers)
sum= 0
sums = 0
for i in range(l):
    sum += numbers[i]

if (sum%3 == 0) & (0 in numbers):
    numbers.sort(reverse=True)
    for i in range(l):
       sums += numbers[i]*(10**(l-i-1))
    print(sums)
else:
    print(-1)
