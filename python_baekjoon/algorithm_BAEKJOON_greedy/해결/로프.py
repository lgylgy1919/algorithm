count = int(input())
lists = []
for i in range(count):
    a = int(input())
    lists.append(a)
lists.sort()

weight = []
n = 0
for i in range(count):
    max_weight = lists[n]*(count-n)
    weight.append(max_weight)
    n += 1

print(max(weight))

