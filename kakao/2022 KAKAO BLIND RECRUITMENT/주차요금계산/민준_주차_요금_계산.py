'''
기본시간(180분) = 5000
그 이후 단위시간에 따라 10분당 += 600
IN과 짝이 맞는 OUT이 없다면 무조건 23:59로 적용한다.
답은 차량번호가 작은 순으로 출력한다.
입/출차 기록의 길이가 짝수가 아니면 23:59 추가한다.
'''

def solution(fees, records):
    answer = []
    inout, time = {}, {}

    # 누적 시간 저장만
    for record in records:
        record = record.split(' ')
        if record[2] == 'IN':
            inout[record[1]] = record[0]
        else:
            before = time.get(record[1], 0)
            time[record[1]] = before + calc_time(inout[record[1]], record[0])
            del inout[record[1]]

    # 남은 차들
    for car, t in inout.items():
        before = time.get(car, 0)
        time[car] = before + calc_time(t, '23:59')
        print(time[car])

    # 요금 계산
    time = list(time.items())
    time.sort(key=lambda x:x[0])
    for car, t in time:
        fee, t = fees[1], t-fees[0]
        if t > 0:
            fee += (t//fees[2]) * fees[3] + (0 if t % fees[2]==0 else fees[3])
        answer.append(fee)

    return answer


def calc_time(t1, t2):
    return int(t2[:2])*60 + int(t2[3:]) - int(t1[:2])*60 - int(t1[3:])
