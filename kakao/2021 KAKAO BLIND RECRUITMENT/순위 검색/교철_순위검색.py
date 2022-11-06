# 유효성 검사 0점..
def info_space(arr):
    info_list = []
    for i in range(len(arr)):
        info_list.append(arr[i].split(' '))
    return info_list


def query_space(arr):
    query_list = arr.split(' ')
    return_list = []
    for i in query_list:
        if i != 'and':
            return_list.append(i)
    return return_list


def solution(info, query):
    answer = [0] * len(query)
    # 정보들
    info_list = info_space(info)
    cnt = 0
    # 조건들
    for i in range(len(query)):
        query_list = query_space(query[i])
        # print(query_space(query[i]))
        for x in range(len(info_list)):
            flag = 1
            for y in range(len(query_list)-1):
                # flag가 없으면 바로 컫
                if not flag:
                    break
                # '-' 일때 패스
                if query_list[y] == '-':
                    pass
                elif info_list[x][y] != query_list[y]:
                    flag = 0
            # 바로 위 for문이 끝났을 때 flag가 살아있다면 cnt +1
            else:
                if flag and int(info_list[x][-1]) >= int(query_list[-1]):
                    answer[i] += 1

    return answer

# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))