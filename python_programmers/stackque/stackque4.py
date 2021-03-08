priorities = [2, 1, 3, 2]
# priorities = [1, 1, 9, 1, 1, 1]
location = 2
# location = 0

sets = []
complete = []
length = len(priorities)


for i in enumerate(priorities):
    sets.append(i)
# [(0, 2), (1, 1), (2, 3), (3, 2)]

while len(complete) != length:\
    
    if priorities[0] == max(priorities):
        complete.append(sets.pop(0))
        priorities.pop(0)
    else:
        sets.append(sets.pop(0))
        priorities.append(priorities.pop(0))

for i, n in complete:
    if i == location:
        answer = complete.index((i, n)) + 1
        break

print(answer)
