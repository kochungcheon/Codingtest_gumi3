'''

이진 트리 문제. 트리를 BFS돌리기 위해 간선 연결된 형식으로 바꾸어 줌.
visted 에 양 총 개수를 체크 한다.

tuple 사용을 참고하였습니다.


'''



from collections import deque

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for a,b in edges:
        tree[a].append(b)
    q = deque([(1,0,tuple([1]+[0]*(len(info)-1)))])
    visited = set()

    while q:
        s,w,visit = q.popleft()
        if s == w:
            continue
        if (s,w,visit) in visited:
            continue
        visited.add((s,w,visit))

        for i in range(len(info)):
            if visit[i] == 1:
                for j in tree[i]:
                    if not visit[j]:
                        temp = list(visit)
                        temp[j] = 1
                        if info[j] == 0:
                            q.append((s+1,w,tuple(temp)))
                        else:
                            q.append((s,w+1,tuple(temp)))
    return max(visited)[0]