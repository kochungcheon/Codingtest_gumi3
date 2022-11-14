# 플로이드 워셜 이용
def solution(n, s, a, b, fares):
    INF = int(1e9)
    ans = INF
    distance_list = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(n):
        distance_list[i][i] = 0
    for fare in fares:
        n1, n2, fee = fare
        distance_list[n1][n2] = fee
        distance_list[n2][n1] = fee

    for i in range(n):  # i : 거치는 지점
        for j in range(n):  # j : 시작하는 지점
            for k in range(n):  # k : 도착지점
                distance_list[i][j] = min(distance_list[i][j], distance_list[i][k] + distance_list[j][k])
                # 각 지점에 대하여 최소값 갱신

    for i in range(n):
        ans = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], ans)

    return ans

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))