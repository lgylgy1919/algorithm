num = int(input())
start = 1
sum = 0
while(start<=num):
    if (start%2 == 0):
        sum += start
        start += 1 
    else:
        start += 1

print(sum)