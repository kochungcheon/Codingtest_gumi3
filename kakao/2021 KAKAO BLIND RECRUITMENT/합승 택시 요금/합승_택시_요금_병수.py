import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    ans = INF
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for fare in fares:
        n1, n2, x = fare
        graph[n1].append((n2, x))
        graph[n2].append((n1, x))
    # 노드, 요금 정보 저장
    # 다잌스트라
    def dijkstra(s):
        q = []
        distance = [INF] * (n + 1)
        # 최단 거리 테이블 무한대로 설정
        heapq.heappush(q, (0, s))
        # 금액, 노드번호
        distance[s] = 0
        # 시작노드 최단거리는 0으로 지정
        while q:
            d, now = heapq.heappop(q)
            if distance[now] < d:
                continue
            # 현재 노드가 이미 확인되었으면 넘어가기
            for g in graph[now]:
                cost = d + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        return distance

    distance_list = [[]]
    for i in range(1, n+1):
        distance_list.append(dijkstra(i))

    for i in range(1, n + 1):
        ans = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], ans)

    return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))