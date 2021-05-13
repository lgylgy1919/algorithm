gems = ["DIA", "EM", "EM", "RUB", "DIA"]
size = len(set(gems)) # 필요한 보석의 종류
dic = {gems[0]: 1} # 모든 보석이 포함되어 있는지 판단하는 용도. set을 사용하는것보다 더 유용
temp = [0, len(gems) - 1] # 최종 정답 후보 구간
start, end = 0, 0
# 0,0 부터 시작해서 오른쪽 포인터를 이동시켜보면서 모든 보석이 포함 되는 구간을 찾아본다.
# 모든 보석이 포함되어 있는 구간을 찾으면 이제 구간을 좁혀본다. 즉, 왼쪽 포인터를 이동시키면서 구간을 축소시켜본다.

while start < len(gems) and end < len(gems):
    # 일단 모든 보석들이 dic에 포함은 되어 있음. 최적인지(가장 작은 범위)인지 부터 체크해야한다.
    # 최적인지 체크하는 것은 최신화 과정을 거친다. 
    if len(dic) == size지
        
        # 기존에 저장되어 있는 구간보다 더 짧은지 아닌지 점검. 더 짧으면 짧은걸로 교체하고아니면 유지
        if end - start < temp[1] - temp[0]:
            temp = [start, end]

        # 최소 조건을 만족한다면 왼쪽 포인터를 이동시켜본다. 최적화를 위해 범위를 더 좁혀본다.(더 짧은 구간을 설정해 본다.)
        if dic[gems[start]] == 1:
            del dic[gems[start]]
        else:
            dic[gems[start]] -= 1
        start += 1


    # 아직 모든 보석을 포함하고 있지 못한다. 그럴 경우 하나씩 dic에 추가한다. end를 오른쪽으로 이동하여 넓혀 간다. 끝까지 찾아 나가는 과정
    else:
        end += 1
        if end == len(gems):
            break
        if gems[end] in dic.keys():
            dic[gems[end]] += 1
        else:
            dic[gems[end]] = 1

print(temp[0] + 1, temp[1] + 1)
