import collections


def findItinerary1(tickets):
    graph = collections.defaultdict(list)
    print(graph)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    print(sorted(tickets))
    print(graph)
    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")
    # 다시 뒤집어서 어휘순 결과로
    print(route[::-1])
    return route[::-1]


tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]
findItinerary1(tickets1)

def findItinerary2(tickets):
    graph = collections.defaultdict(list)
    # 그래프를 뒤집어서 구성 
    for a, b in sorted(tickets, reverse=True)
        graph[a]:append(b)

    route = []
    def dfs(a):
        while graph[a]:
            # 마지막 값을 읽어 어휘 순 방문 
            dfs(graph[a].pop())
        route.append(a)

    dfs('JKF')
    # 다시 뒤집어 어휘 순 결과로 
    return route[::-1]



def findItinerary3(tickets):
    graph=collections.defaultdict(list)
    #그래프 순서대로 구성 
    for a,b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ["JFK"]
    while stack:
        #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리 
        while graph[stack[-1]]:
            stack.append(graph[stack[-1].pop(0)])
        route.append(stack.pop())

    #다시 뒤집어 어휘 순 결과로 
    return route[::-1]