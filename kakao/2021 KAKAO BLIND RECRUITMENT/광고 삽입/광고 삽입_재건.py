'''
주어지는 시간을 초 단위로 변환
최대 시간 100시간 => 360,000초

누적합 imos 알고리즘 활용

광고 시간 범위 안의 합이 최대인 값의 시작 지점을 시간으로 출력

시간복잡도 O(n)
'''


def to_second(time):
    tmp = list(map(int, time.split(':')))
    return tmp[0] * 3600 + tmp[1] * 60 + tmp[2]


def to_time(sec):
    h = sec // 3600
    sec = sec % 3600
    if h < 10:
        h = '0' + str(h)
    m = sec // 60
    if m < 10:
        m = '0' + str(m)
    s = sec % 60
    if s < 10:
        s = '0' + str(s)
    return f'{h}:{m}:{s}'


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = to_second(play_time)
    adv_time = to_second(adv_time)
    time_range = [0] * (play_time + 1)
    adv_possible_time = play_time - adv_time

    i = 0
    for time in logs:
        start, end = time.split('-')
        logs[i] = [to_second(start), to_second(end)]
        time_range[logs[i][0]] += 1
        time_range[logs[i][1]] -= 1
        i += 1
    for i in range(1, play_time):
        time_range[i] += time_range[i-1]
    logs.sort(key=lambda x: (x[1], x[0]))


    # for문 탐색을 logs가 아닌 time_range로 해서 최댓값을 찾았어야 함
    # logs로 탐색을 시도하니 조건에 맞지 않는게 있어 틀린 예제 발생
    # 또한 슬라이싱을 매번 사용해서 sum을 하여 시간초과 발생 ([시작점] 빼고 [끝점 +1] 부분을 더 해주며 총합 구하기)

    if logs[0][0] > adv_possible_time:
        sec = logs[-1][1] - adv_time
        if sec < 0:
            sec = 0
    else:
        max_v = 0
        sec = 0
        for i in range(len(logs)):
            if logs[i][0] <= adv_possible_time:
                accumulate_sum = sum(time_range[logs[i][0]:logs[i][0] + adv_time + 1])
                if max_v < accumulate_sum:
                    max_v = accumulate_sum
                    sec = logs[i][0]
            else:
                break

    answer = to_time(sec)
    # answer = '%02d:%02d:%02d' % (sec/3600, sec/60%60, sec%60) 위 함수와 같은 값 출력

    return answer
