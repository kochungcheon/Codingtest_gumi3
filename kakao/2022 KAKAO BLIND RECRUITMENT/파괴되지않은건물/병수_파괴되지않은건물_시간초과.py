board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
answer = 0


N = len(board)
M = len(board[0])
S = len(skill)
for m in range(S):
    if skill[m][0] == 1:
        for i in range(skill[m][1], skill[m][3]+1):
            for j in range(skill[m][2], skill[m][4]+1):
                board[i][j] -= skill[m][5]
    else:
        for i in range(skill[m][1], skill[m][3]+1):
            for j in range(skill[m][2], skill[m][4]+1):
                board[i][j] += skill[m][5]
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            answer += 1
print(answer)
print(board)

'''
O(N^3)
'''
'''
정답은 맞는데 시간 두개 터짐
'''
