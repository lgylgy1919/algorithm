'''
각 작업의 배포 가능 일자를 구해서 새로운 리스트 만들기
# [93, 30, 55]   [95, 90, 99, 99, 80, 99]
# [1, 30, 5]      [1, 1, 1, 1, 1, 1]
# [7, 2, 9]     [5, 10, 1, 1, 20, 1]
# [2, 1]         [1,3,2]

'''
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
release = []
answer = []


# release 도출
for i in range(len(progresses)):
    complete = (100-progresses[i]) // speeds[i]
    if(100-progresses[i]) % speeds[i] != 0:
        complete += 1
    release.append(complete)


# answer 구하기
point = release[0]
j = 1
days = 1
while j < len(release):
    if point >= release[j]:
        days += 1
        j += 1
    elif point < release[j]:
        point = release[j]
        answer.append(days)
        days = 1
        j += 1

    if j == len(release):
        answer.append(days)


print(release)
print(answer)
