'''

시간 복잡도는 O(N)
자료 구조를 활용하는 문제.
set을 통해 최초로 받는 신고들을 중복 제거 해주었다.
for 문을 순회 하면서
setdefault() 를 활용하는 방법 도 있지 않을 까 생각했습니다.

'''


def solution(id_list, report, k):
    reports = list(set(report))
    answer = [0] * len(id_list)
    report_dict = {}
    idx = {}
    for i in range(len(id_list)):
        report_dict[id_list[i]] = []
        idx[id_list[i]] = i
    for report in reports:
        report_dict[report.split(' ')[1]].append(report.split(' ')[0])
    for value in report_dict.values():
        if len(value) >= k:
            for j in value:
                answer[idx[j]] += 1
    return answer