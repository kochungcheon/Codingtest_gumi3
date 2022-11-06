'''
문제 해결 방법
1. 받아온 info와 query를 계산에 편한 형태의 list로 바꿔준다.
2. 기능별로 함수를 분리하는 걸 연습하기 위해
   (1) 가능한 지원자의 모든 경우의 수를 만드는 함수와
   (2) 그에 맞는 지원자들의 점수를 저장하는 list를 만드는 함수 두 종류를 만들었다.
3. 그러나 모든 경우의 수를 확인하다보니 시간복잡도 측면에서 불리해져 '효율성'은 1/4만 합격했다.
4. 시간 복잡도 문제를 해결하기 위해 이진탐색을 수행하는 함수를 맨 나중에 추가했다.
'''

def solution(info, query):
    # 받아온 지원자 info를 [지원자 정보, 점수] 단위로 저장할 새 list
    new_info = []
    # new_info = [['jbjp', 150], ['pfsc', 210], ['pfsc', 150], ['cbsp', 260], ['jbjc', 80], ['pbsc', 50]])
    for i in range(len(info)):
        info[i] = info[i].split(' ')
        info_str = ''
        temp = []
        for j in range(4):
            info_str += info[i][j][0]
        temp.append(info_str)
        temp.append(int(info[i][-1]))
        new_info.append(temp)

    # 받아온 query를 [문자열, 점수] 단위로 저장할 새 list
    new_query = []
    # new_query = [['jbjp', 100], ['pfsc', 200], ['c-sp', 250], ['-bs-', 150], ['---c', 100], ['----', 150]])
    # 앞에거 하나 java, backend, junior, pizza, 100점 이상
    for i in query:
        query_other = i.split(' and ')
        temp = query_other[-1].split(' ')
        query_other[-1] = temp[0]
        score = int(temp[1])
        temp_arr = []
        temp_str = ''
        for j in query_other:
            temp_str += j[0]
        temp_arr.append(temp_str)
        temp_arr.append(score)
        new_query.append(temp_arr)

    dict = applicant_list()                                   # 만들 수 있는 지원자의 모든 경우의 수 108개
                                                              # language * job * career * food
    score_arr = [[] for i in range(4*3*3*3)]                  # query를 통과한 지원자의 점수를 저장하는 list

    for i in new_info:
        score_arr = applicant_score_list(i, dict, score_arr)  #

    for i in range(len(score_arr)):
        score_arr[i].sort()  # 점수순으로 sort해준다.

    answer = []

    for i in new_query:
        num_arr = score_arr[dict.index(i[0])]
        count = 0
        low = binary_search(0, len(num_arr), i[1], num_arr)
        answer.append(len(num_arr) - low + 1)

    return answer


# 가능한 지원자의 모든 경우의 수를 만드는 함수
def applicant_list():
    languages = ['-', 'c', 'j', 'p']
    jobs = ['-', 'b', 'f']
    careers = ['-', 'j', 's']
    foods = ['-', 'c', 'p']

    dict = []
    temp_string = ''
    for language in languages:
        for job in jobs:
            for career in careers:
                for food in foods:
                    temp_string += language + job + career + food
                    dict.append(temp_string)
                    temp_string = ''

    return dict


# 위에서 만든 경우의 수(query)를 만족하는 지원자들의 점수 list
def applicant_score_list(info, dict, score_arr):
    languages = ['-']
    if info[0][0] != '-':
        languages.append(info[0][0])
    jobs = ['-']
    if info[0][1] != '-':
        jobs.append(info[0][1])
    careers = ['-']
    if info[0][2] != '-':
        careers.append(info[0][2])
    foods = ['-']
    if info[0][3] != '-':
        foods.append(info[0][3])

    temp_str = ''
    for language in languages:
        for job in jobs:
            for career in careers:
                for food in foods:
                    temp_str += language + job + career + food
                    score_arr[dict.index(temp_str)].append(info[1])
                    temp_str = ''

    return score_arr


# 효율성 문제를 해결하기 위한 이진탐색
def binary_search(s, e, d, arr):
    while s < e:
        mid = (s+e)//2

        if arr[mid] < d:
            s = mid+1

        else:
            e = mid

    return e+1


# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
#
# print(solution(info, query))