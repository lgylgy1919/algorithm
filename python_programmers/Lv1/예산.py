d = [2, 2, 3, 3]
budget = 10

d.sort()
num = 0
for i in d:
    budget -= i
    num += 1
    if budget < 0:
        num -= 1
        break

print(num)
