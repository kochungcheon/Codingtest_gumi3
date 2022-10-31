'''
최적해를 구하는 것이므로 dfs로 풀기로 마음먹음
(시간복잡도가 10!이므로 완전탐색으로 풀어도 지장은 없음)

문제 해결방법은 diff가 max_diff보다 큰지 아닌지를 먼저 확인하고
만약 diff가 max_diff와 같다면 answer_list(정답 가능성이 있는 배열)에 모아준다.

그 후 answer_list의 길이가 0이라면 이기는 경우가 없었던 것으로 판단하여 -1을 return 해주고
answer_list의 길이가 2 이상이라면 문제에서 제시하는 정답(낮은 점수를 더 많이 맞춘경우)을
return 해주기 위해 solution함수를 정의했다.
'''
answer_list = [], max_diff = 0

# n: 남은 화살 ryan: 라이언이 맞춘 화살 peach: 피치가 맞춘 화살 i: 시기
def dfs(n, ryan, apeach, i):
    global max_diff      # 최대 점수차
    global answer_list   # 가능한 결과들을 모아놓을 list

    # 화살이 없는 경우 or 화살이 있고 마지막 시기
    if n == 0 or (n > 0 and i == 10):
        ryan_score = 0
        apeach_score = 0

        if i == 10:       # 마지막 화살을 쏠 때 지정한다.
            ryan[10] = n

        # 점수 비교에 0점은 계산할 필요가 없으므로 1~10점만 계산한다. (10점부터 계산)
        for j in range(10):
            if ryan[j] > 0:
                if ryan[j] > apeach[j]:
                    ryan_score += 10-j
            if apeach[j] > 0:
                if apeach[j] >= ryan[j]:
                    apeach_score += 10-j

        diff = ryan_score - apeach_score

        # 최대 차이와 현재 차이가 같으면 가능한 정답 list에 해당 경우를 추가해준다.
        # 차이가 0이면 우리에게 필요한 정보가 아니므로 제외

        if diff == max_diff and diff != 0:
            max_diff = diff
            answer_list.append(ryan.copy())

        # 현재 차이가 최대 차이보다 크면
        # 최대값과 정답 리스트를 새롭게 갱신해준다.
        if diff > max_diff:
            max_diff = diff
            answer_list = [ryan.copy()]

        return

    # 나머지 경우들
    if n > 0 and i < 10:
        # 라이언이 어피치보다 한발 더 맞춘 경우
        ryan[i] = apeach[i]+1
        dfs(n-ryan[i], ryan.copy(), apeach, i+1)

        # 그 외의 경우
        ryan[i] = 0
        dfs(n, ryan.copy(), apeach, i+1)

def solution(n, info):
    ryan = [0] * 11
    dfs(n, ryan.copy(), info, 0)

    if len(answer_list) == 0:
        return [-1]

    else:
        for c in answer_list:
            c.reverse()

        answer_list.sort(reverse=True)
        answer_list[0].reverse()

        return answer_list[0]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n, info))