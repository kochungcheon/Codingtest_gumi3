'''
누적합 - imos 문제입니다
초를 기준으로 배열을 만들어 주었습니다.
시청시작에 +1 시청종료에 -1을한다음
누적함 계산을 해주었습니다.
누적합 계산 편의상 패딩을 넣어주었습니다.
시간 복잡도는 O(N)
'''




def to_seconds(time):
    return sum([int(x)*y for x, y in zip(time.split(':'), [3600, 60, 1])])

def to_time(seconds):
    h, m = divmod(seconds, 3600)
    m, s = divmod(m, 60)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def solution(play_time, adv_time, logs):
    # 초로 변환
    play_sec = to_seconds(play_time)
    adv_sec = to_seconds(adv_time)

    # 누적합을 계산
    prefix = [0 for _ in range(360001)]
    for log in logs:
        log = log.split("-")
        prefix[(to_seconds(log[0]))] += 1
        prefix[(to_seconds(log[1]))] -= 1

    for idx in range(1, play_sec + 1):
        prefix[idx] += prefix[idx - 1]
    for idx in range(1, play_sec + 1):
        prefix[idx] += prefix[idx - 1]

    ans = 0
    max_sum_played = prefix[adv_sec]
    for start_time in range(1, play_sec):
        end_time = start_time + adv_sec if start_time + adv_sec < play_sec else play_sec
        sum_played = prefix[end_time] - prefix[start_time]
        if max_sum_played < sum_played:
            max_sum_played = sum_played
            ans = start_time + 1
    return to_time(ans)