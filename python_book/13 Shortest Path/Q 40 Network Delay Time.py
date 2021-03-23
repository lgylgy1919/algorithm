import collections
import heapq


def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    # 그래프 인접리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수 : [(소요시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        print("time=", time, "node =", node)
        if node not in dist:
            dist[node] = time
            print("dist=", dist)
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                print("Q=", Q)

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        print(dist)
        print(max(dist.values()))
        return max(dist.values())
    return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2

networkDelayTime(times, N, K)
