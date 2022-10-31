'''

문자열 문제

리스트에 숫자를 저장 하는 방식으로 해결. 문자열을 2개씩 짤라서 시간을 계산.
23:59 기준으로 들어온 시간에 따라 계산
시간 복잡도는 O(N)

'''



def cal(time, fees):
    if time <= fees[0]:
        return fees[1]
    q = (time - fees[0] + fees[2] - 1) // fees[2]
    return q * fees[3] + fees[1]


def solution(fees, records):
    cnt = [0] * 10010
    stored = [-1] * 10010
    for record in records:
        s, num, state = record.split()
        time = int(s[:2]) * 60 + int(s[3:])
        num = int(num)
        if state == "IN":
            stored[num] = time
        else:
            cnt[num] += time - stored[num]
            stored[num] = -1

    for i in range(10000):
        if stored[i] != -1:
            cnt[i] += 23*60+59 - stored[i]
    ans_lst = [cal(t, fees) for t in cnt if t != 0]
    return ans_lst