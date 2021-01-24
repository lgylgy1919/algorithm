n = int(input())
lists = list(map(int, input().split()))
lists.sort()
sum = []
answer = 0
sum.append(lists[0])

for i in range(1, len(lists)):
    temp = lists[i] + sum[i - 1]
    sum.append(temp)

if lists[0] != 1:
    print("1")

for num in range(1, len(lists) - 1):
    if sum[num] + 1 < lists[num + 1]:
        answer = sum[num] + 1
        print(answer)
        break
if answer == 0:
    answer = sum[len(sum) - 1] + 1
    print(answer)


# lists로 만들 수 있는 모든 경우의 무게를 구한다.
# 오름차순으로 정렬한다.

# 중복을 제거한다.
# 1이 포함되어있는지 확인한다.
# 1이 없으면 1 출력
# 1이 있으면 연속하지 않는 부분 찾기
# 마지막 항을 비교하기 위한 방법 찾기

N = int(input())
weight_list = sorted(list(map(int, input().split())))
m_sum = 1

for i in range(N):
    if m_sum < weight_list[i]:
        break
    m_sum += weight_list[i]
print(m_sum)
