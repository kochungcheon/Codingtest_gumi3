'''

조합과 중복제거를 통해 문제 해결하였습니다.
시간 복잡도는 O(MN)

'''


from itertools import combinations
def solution(orders, course):
    check = []
    for order in orders:
        for i in course:
            check += (list(combinations(list(order),i)))

    result = []

    set_l = list(set(check))
    for i in course:
        answer = []
        set_list = [k for k in set_l if len(k) == i]
        for j in set_list:
            count = 0
            for order in orders:
                ok = True
                for menu in j:
                    if menu not in order:
                        ok = False
                        break
                if ok == True:
                    count += 1

            if count >= 2:
                answer.append(("".join(aa for aa in sorted(j)),count))

        if len(answer)>0:
            answer.sort(key = lambda x: -x[1])
            choice =  answer[0][1]
            for candidate in answer:
                if candidate[1] == choice:
                    result.append(candidate[0])


    return sorted(list(set(result)))