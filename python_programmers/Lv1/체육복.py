'''
모든 학생이 하나씩 있다고 가정.
lost에서 하나씩 빼고
reserve에서 하나씩 더하고
앞에서 하나씩 있는지 없는지 확인, 
'''
n = 3
lost = [3]
reserve = [1]
# return = 5

students = [1]*n
for i in lost:
    students[i-1] -= 1

for j in reserve:
    students[j-1] += 1

print(students)

for k in range(n-1):
    if students[k] == 2 and students[k+1] == 0:
        students[k], students[k+1] = 1, 1
    elif students[k] == 0 and students[k+1] == 2:
        students[k], students[k+1] = 1, 1


print(students)

answer = 0
for i in students:
    if i != 0:
        answer += 1
print(answer)
