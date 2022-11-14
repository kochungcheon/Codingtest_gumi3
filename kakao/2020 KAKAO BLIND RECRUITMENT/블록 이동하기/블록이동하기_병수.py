from collections import deque


def solution(board):
    N = len(board)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque([(0, 0, 1, 0)])
    visited = {(0, 0, 1)}

    while q:
        x, y, direction, mv = q.popleft()
        nx, ny = x + dx[direction], y + dy[direction]
        if nx == N - 1 and ny == N - 1:
            return mv

        # 네 방향으로 이동
        for d in range(4):
            nx1, ny1 = x + dx[d], y + dy[d]
            nx2, ny2 = nx + dx[d], ny + dy[d]
            if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                # 이미 방문했거나 한 칸이라도 벽인 경우
                if (nx1, ny1, direction) in visited or board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
                    continue
                # 현재 방향을 유지한채로 상하좌우로 이동
                q.append((nx1, ny1, direction, mv + 1))
                visited.add((nx1, ny1, direction))
                # 회전
                rotated_d = (direction + 1) % 2
                # 로봇 세로 + 오른쪽으로 회전, 로봇 가로 + 아래쪽으로 회전
                if direction + d == 1:
                    if (x, y, rotated_d) not in visited:
                        q.append((x, y, rotated_d, mv + 1))
                        visited.add((x, y, rotated_d))
                    if (nx, ny, rotated_d) not in visited:
                        q.append((nx, ny, rotated_d, mv + 1))
                        visited.add((nx, ny, rotated_d))
                # 로봇 세로 + 왼쪽으로 회전, 로봇 가로 + 위쪽으로 회전
                elif direction + d == 3:
                    if (nx1, ny1, rotated_d) not in visited:
                        q.append((nx1, ny1, rotated_d, mv + 1))
                        visited.add((nx1, ny1, rotated_d))
                    if (nx2, ny2, rotated_d) not in visited:
                        q.append((nx2, ny2, rotated_d, mv + 1))
                        visited.add((nx2, ny2, rotated_d))
    return -1

