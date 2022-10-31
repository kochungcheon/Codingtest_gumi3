'''
주어진 입출력을 내 입맛에 맞게 바꾸는것이 먼저
report는 이용자id : 신고한 id 형태의 list이므로 문제를 풀기 위해
answer_dict를 만들어 신고당한사람 : [신고자1, 신고자2] 형태로 만든다.

단, 중복된 신고는 의미가 없으므로 list(set())을 통해 중복인자를 제거하고 풀이했다.
'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    # 중복된 신고 제거
    report_list = list(set(report))
    answer_dict = {}  # 신고당한사람 : [신고자1, 신고자2] 형태의 dict

    # id_list에 있는 아이디를 answer_dict에 key 값으로 넣어줌
    for i in id_list:
        answer_dict[i] = []

    # report_list에 있는 "이용자id 신고한id"형태의 문자열을 answer_dict에 넣어줌
    for i in report_list:
        string = i.split(" ")
        answer_dict[string[1]] += [string[0]]

    # k번 이상 신고된 사람 check
    for key, value in answer_dict.items():
        if len(value) >= k:
            for person in value:
                answer[id_list.index(person)] += 1

    return answer, answer_dict

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))