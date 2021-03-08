n = int(input())
x = 0
for i in range(n):
    lists = list(input())
    new_lists = []
    if len(lists)<=2:
        x+=1
    else:
        for t in range(len(lists)-1):
            if lists[t] != lists[t+1]:
                new_lists.append(lists[t])
        new_lists.append(lists[len(lists)-1])    
        if len(new_lists) == len(set(new_lists)):
            x+=1


print(x)
'''
조건1) 한 글자는 무조건 그룹 단어
조건2) 두 글자는 무조근 그룹 단어

다음 글자가 같으면 리스트에서 제거
or 다음 글자가 다르면 새 리스트에 추가

수정된 리스트에서 중복된 글자가 있는지 체크

set() 중복 제거 //
for 문 + if 문(if a not in list / if a in list)
'''