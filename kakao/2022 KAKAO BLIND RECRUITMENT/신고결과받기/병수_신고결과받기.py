def solution(id_list, report, k):
    # 1
    report = set(report)
    # 2
    answer = {x: 0 for x in id_list}
    report_count = {x: 0 for x in id_list}
    # 3
    for r in report:
        report_count[r.split()[1]] += 1
    # 4
    for r in report:
        if report_count[r.split()[1]] >= k:
            answer[r.split()[0]] += 1
    # 5
    return list(answer.values())


'''
딕셔너리르 통해 카운팅을 해주었다.
1. 한 유저가 여러번 신고는 가능하나 동일한 유저에 대하여 신고 횟수는 1회로 처리하기 때문에 
set을 통하여 중복을 제거 해주었다.
2. answer, report_count 딕셔너리를 id_list의 요소들로 딕셔너리를 만들어주었다.
3. report_count에 각 사람이 신고 받은 횟수에 대하여 카운팅을 해주었다.
4. 완성된 report_count에서 value값이 k보다 크거나 같을 경우
메일을 받을 사람에게 전송할 횟수를 증가시켜주었다.
5. 정답은 list형태이기에 list를 통하여 출력해주었다.
'''
'''
O(N)
'''