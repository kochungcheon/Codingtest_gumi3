'''
1 <= n <= 1000
0. 대문자 to 소문자
1. 제외한 문자 제거 n탐색
2. n탐색하면서 . 만나면 flag로 나머지 연속된 . => ''
.이 아니면 flag 초기화
3. strip으로 양끝 . 제거
4. 빈 문자열이라면 "a"
5. 15자 까지만 입력 받기
6. rstrip으로 마지막 . 있으면 제거
7. 만약 2자 이하면 3이 될 때까지 append(id[-1])
시간복잡도 O(n)
'''

def solution(new_id):
    answer = ''
    remove_str = '~!@#$%^&*()=+[{]}:?,<>/'
    # 1.
    new_id = new_id.lower()
    # 2.
    new_id = list(new_id)
    for i in range(len(new_id)):
        if new_id[i] in remove_str:
            new_id[i] = ''
    new_id = list(''.join(new_id))
    # 3.
    flag = False
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if flag:
                new_id[i] = ''
            else:
                flag = True
        else:
            flag = False
    # 4.
    answer = ''.join(new_id)
    answer = answer.strip('.')
    # 5.
    if answer == '':
        answer = 'a'
    # 6.
    answer = answer[:15]
    answer = answer.rstrip('.')
    # 7.
    while len(answer) < 3:
        answer += answer[-1]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("a.$.a"))


