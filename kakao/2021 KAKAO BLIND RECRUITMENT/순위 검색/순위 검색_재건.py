'''
지원자 정보와 같은 형태로 문의조건을 변환하고 지원자 정보들을 돌면서 조건을 만족하는 지원자를 더 해준다.
시간복잡도 O(MN)
M = 50,000 N = 100,000
최대 크기일 경우 시간 초과이나
효율성을 위한 코드 만들기 실패 ㅜㅜ
정확성만 통과
'''


def solution(info, query):
    answer = [0] * len(query)
    for i in range(len(info)):
        info[i] = list(info[i].split())
    for i in range(len(query)):
        query[i] = list(query[i].split())
        query[i] = [query[i][0], query[i][2], query[i][4], query[i][6], query[i][7]]

        for j in range(len(info)):
            flag = True
            for k in range(4):
                if query[i][k] != info[j][k] and query[i][k] != '-':
                    flag = False
                    break
            if flag:
                if int(query[i][4]) <= int(info[j][4]):
                    answer[i] += 1

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
