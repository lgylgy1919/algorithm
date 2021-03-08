arr = [4, 4, 4, 3, 3]

answer = []

for i in arr:
    answer.append(i)
    if len(answer) > 1 and answer[-2] == answer[-1]:
        del answer[-1]

print(answer)
