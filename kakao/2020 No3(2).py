gems = ["A", "A", "B"]
size = len(set(gems))
dic = {gems[0]: 1}
temp = [0, len(gems) - 1]
start, end = 0, 0

while start < len(gems) and end < len(gems):
    #
    if len(dic) == size:
        if end - start < temp[1] - temp[0]:
            temp = [start, end]
        if dic[gems[start]] == 1:
            del dic[gems[start]]
        else:
            dic[gems[start]] -= 1
        start += 1

    # 아직 모든 보석을 포함하고 있지 못한다. 그럴 경우 하나씩 dic에 추가한다.
    else:
        end += 1
        if end == len(gems):
            break
        if gems[end] in dic.keys():
            dic[gems[end]] += 1
        else:
            dic[gems[end]] = 1