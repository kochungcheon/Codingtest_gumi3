'''
신고하고, 처리 결과를 메일로 발송
유저 별로 처리 결과 메일을 받은 횟수
제한시간 10초

report - 공백을 기준으로 "신고자 신고받은사람"

조건
한 유저는 다른 유저에 대해 중복 신고 안된다.
k번 신고 받은 사람은 이용이 정지 되며
정지 되는 순간 해당 사람을 신고한 사람에게 메일 발송

20만번 탐색, 중복 제거로 다시 탐색
O(n)
'''


def solution(id_list, report, k):
    len_id = len(id_list)
    report_user = [set() for _ in range(len_id)]
    mail = [0] * len_id
    for report_one in report:
        repo, stop = report_one.split()
        report_user[id_list.index(stop)].add(repo)
    for users in report_user:
        if len(users) >= k:
            for user in users:
                mail[id_list.index(user)] += 1

    answer = mail
    return answer


# 	["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
