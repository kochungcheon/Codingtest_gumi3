'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

-_.~!@#$%^&*()=+[{]}:?,<>/ 중에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
'''
# 22, 23 런타임에러
def solution(new_id):
    answer = ''
    if not new_id:
        new_id = 'a'

    # 1.
    id = new_id.lower()
    # 2.
    id_list = []
    for i in id:
        # 알파벳이면 append
        if i in list(filter(str.isalpha, id)):
            id_list.append(i)
        # 숫자면 append
        elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            id_list.append(i)
        # 기호 안에 들어가면 append
        elif i in ['-', '_', '.']:
            id_list.append(i)
    # 리스트가 비었다면 'a' append
    if not id_list:
        id_list.append('a')

    # 3 / 4
    not_dot_list = []
    if len(id_list) > 1:
        for i in range(1, len(id_list)):
            # 3 / 4
            if id_list[i - 1] == '.' and id_list[i] == '.':
                pass
            else:
                not_dot_list.append(id_list[i - 1])
        # 4
        if id_list[-1] != '.':
            not_dot_list.append(id_list[-1])
    else:
        not_dot_list.append(id_list[0])

    if not_dot_list[0] == '.':
        not_dot_list.pop(0)

    if not not_dot_list:
        not_dot_list.append('a')

    # 6
    if len(not_dot_list) >= 16:
        not_dot_list = not_dot_list[:15]
        if not_dot_list[-1] == '.':
            not_dot_list.pop()

    # 7
    while len(not_dot_list) < 3:
        not_dot_list += not_dot_list[-1]

    answer = ''.join(not_dot_list)
    return answer

# print(solution("1qweqweqweqwe.qwe.qwe..qweqwe..qwe"))