'''

단순 다익스트라 문제입니다.
힙큐를 통해O(nlogn)으로 구현 해서 풀었습니다.
A,B,I 코스 모두 계산 해주어 풀어야 합니다.
https://www.acmicpc.net/problem/1504
사고가 이 문제와 매우 유사합니다.

'''

import heapq, sys


def dijkstra(node_dict, n, start, end):
    heap = [(0, start)]
    visit = [1 << 31 for _ in range(n + 1)]
    visit[start] = 0
    while heap:
        weight, now = heapq.heappop(heap)
        if visit[now] < weight:
            continue
        for node, w in node_dict[now]:
            if visit[node] > weight + w:
                heapq.heappush(heap, (weight + w, node))
                visit[node] = weight + w
    return visit[end]


def solution(n, s, a, b, fares):
    answer = 1 << 31
    node_dict = {x: [] for x in range(n + 1)}
    for start, end, weight in fares:
        node_dict[start].append((end, weight))
        node_dict[end].append((start, weight))
    for i in range(1, n + 1):
        if i == s:
            answer = min(answer, dijkstra(node_dict, n, s, a) + dijkstra(node_dict, n, s, b))

        elif i == a:
            distA = dijkstra(node_dict, n, s, a)
            if distA < answer:
                answer = min(answer, distA + dijkstra(node_dict, n, a, b))

        elif i == b:
            distB = dijkstra(node_dict, n, s, b)
            if distB < answer:
                answer = min(answer, distB + dijkstra(node_dict, n, b, a))

        else:
            distI = dijkstra(node_dict, n, s, i)
            if distI < answer:
                answer = min(answer, distI
                             + dijkstra(node_dict, n, i, a) + dijkstra(node_dict, n, i, b))

    return answer