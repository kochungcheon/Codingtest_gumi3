def build(answer):
    for x, y, s in answer:
        # 기둥인 경우
        if s == 0:
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보인 경우
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
                continue
            if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            return False
    return True


def solution(n, build_frame):
    ans = []
    for i, j, a, b in build_frame:
        # 삭제할 경우
        if b == 0:
            ans.remove([i, j, a])
            if not build(ans):
                ans.append([i, j, a])
        # 설치할 경우
        else:
            ans.append([i, j, a])
            if not build(ans):
                ans.remove([i, j, a])
    return sorted(ans)