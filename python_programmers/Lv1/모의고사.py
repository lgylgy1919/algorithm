student1 = [1, 2, 3, 4, 5]*2000
student2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

answers = [1, 2, 3, 4, 5]

answer = []
cnt = []
st1 = 0
st2 = 0
st3 = 0

for i in range(len(answers)):
    if student1[i] == answers[i]:
        st1 += 1
cnt.append(st1)

for i in range(len(answers)):
    if student2[i] == answers[i]:
        st2 += 1
cnt.append(st2)

for i in range(len(answers)):
    if student3[i] == answers[i]:
        st3 += 1
cnt.append(st3)

print(cnt)
m = max(cnt)
answer = list(i+1 for i, j in enumerate(cnt) if j == m)

print(answer)
