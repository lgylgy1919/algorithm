number = int(input())
waitings = list(map(int,input().split(" ")))
waitings.sort()
min_sum = 0
for i in range(number):
    min_sum+=(waitings[i]*number)
    number -= 1
print(min_sum)
