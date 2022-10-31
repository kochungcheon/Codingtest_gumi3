from collections import deque


def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    # 1
    ans = 1

    for edge in edges:
        tree[edge[0]].append(edge[1])

    dq = deque([[tree[0], 1, 1]])
    while dq:
        x = dq.popleft()
        # 2
        for i, next_node in enumerate(x[0]):
            total = x[2]
            if info[next_node] == 0:
                cal = x[1] + 1
                total += 1

            else:
                cal = x[1] - 1
            # 3
            if cal > 0:
                dq.append([x[0][:i] + x[0][i+1:] + tree[next_node], cal, total])
                ans = max(ans, total)

    return ans


'''
BFS를 활용하는 문제이다.
이진 트리라고 명시되어 있었기에 사이클을 고려하지 않고 문제릂 푸는것에 큰 어려움이 없었다.
1. 루트 노드는 양이기 때문에 answer는 항상 1로 고정을 하고 시작을한다.

2. 값과 인덱스 값을 같이 찾아야 했기에 enumerate를 사용해주었다.

3. 양의 수가 늑대의 수보다 클 때만 최대값을 갱신해주었다.
'''
'''
O(N)
'''
