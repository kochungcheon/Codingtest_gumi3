board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
answer = 0


N = len(board)
M = len(board[0])
ans = 0

damage_arr = [[0]* 1003 for _ in range(1003)]

for s in skill:
    skill_type, x1, y1, x2, y2, damage = s
    if skill_type == 1:
        damage = -damage
    damage_arr[x1][y1] += damage
    damage_arr[x1][y2+1] -= damage
    damage_arr[x2+1][y1] -= damage
    damage_arr[x2+1][y2+1] += damage


for i in range(1, N):
    for j in range(M):
        damage_arr[i][j] += damage_arr[i-1][j]

for i in range(N):
    for j in range(1,M):
        damage_arr[i][j] += damage_arr[i][j-1]

for i in range(N):
    for j in range(M):
        if damage_arr[i][j] + board[i][j] > 0:
            ans += 1

print(ans)

'''
누적합을 구하는 imos기법을 사용하였다.
시작점과 끝점을 기록하여, 그 값으로 휩쓸면서 지나간다고 생각을 해야한다.
md파일 참조
'''
'''
O(N^2)
'''