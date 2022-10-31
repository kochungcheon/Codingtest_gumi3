def solution(fees, records):
    answer = []
    base_time, base_fee, time, fee = fees[0], fees[1], fees[2], fees[3]
    in_car_d = {}
    car_fee = [0] * 10000
    car_num = set()
    cnt = [0] * 10000
    while records:
        car = records.pop(0)
        # t : time, n : number, io : inout
        t, n, io = car.split(' ')
        car_num.add(n)
        h, m = t.split(':')
        tt = (int(h)*60) + int(m)
        if io == 'IN':
            in_car_d[n] = tt
            cnt[int(n)] += 1
        elif io == 'OUT':
            ans = tt - in_car_d[n]
            # answer.append(ans)
            car_fee[int(n)] += ans
            cnt[int(n)] -= 1
    # OUT이 안나와 cnt가 남아있다면 23시 59분에서 IN 시간을 빼줌
    for i in car_num:
        if cnt[int(i)]:
            car_fee[int(i)] += 1439 - in_car_d[i]

    nn = sorted(car_num)
    for i in nn:
        if car_fee[int(i)] > base_time:
            # 저장된 시간이 time에 맞게 안떨어지면
            if (car_fee[int(i)]-base_time) % time:
                answer.append(((car_fee[int(i)]-base_time)//time+1)*fee+base_fee)
            else:
                answer.append(((car_fee[int(i)] - base_time) // time) * fee + base_fee)
        else:
            answer.append(base_fee)

    return answer


# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

