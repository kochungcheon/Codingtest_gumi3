'''
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘

완전탐색
O(MN)

1.
최대 단위는 len(s) // 2 + 1 까지
그 이상은 무조건 1

2.
연속되는 문자열만 압축 가능
문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
'''


def solution(s):
    answer = 1000
    if len(s) < 3:
        answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        ss = s[:i]
        tmp = ''
        cnt = 0
        for j in range(0, len(s), i):
            if s[j:j+i] == ss:
                cnt += 1
            else:
                if cnt != 1:
                    tmp += str(cnt)
                tmp += ss
                ss = s[j:j+i]
                cnt = 1
        if cnt != 1:
            tmp += str(cnt)
        tmp += ss
        answer = min(answer, len(tmp))

    return answer


print(solution("ababcdcdababcdcd"))
