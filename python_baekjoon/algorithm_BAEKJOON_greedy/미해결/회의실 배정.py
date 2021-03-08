'''
회의가 가장 빨리 끝나는 순서
그 다음 시작하는 회의 중 가장 빨리 끝나는 회의

'''
# 리스트 만들기
# 두 번째 인자 오름차순으로 정렬
# 
n = int(input())
lists = []
for i in range(n):
    a = list(map(int,input().split(" ")))
    lists.append(a)

assign = []
a = 0
# 끝나는 순서가 빠른 순서대로 재정렬
lists.sort(key=lambda x:x[1])
# 할당리스트에 분배
assign.append(lists[0])
for i in range(1,n):
    if lists[i][0] >= assign[a][1]:
        assign.append(lists[i])
        a+=1
        
print(len(assign))