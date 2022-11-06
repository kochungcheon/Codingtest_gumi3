'''
명세를 잘 읽자.
'''

def solution(new_id):
    # 1. 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i
    # 3. new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break

    # 4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = answer.strip('.')

    # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == '':
        answer += 'a'

    # 6. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')

    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer) <= 2:
        word = answer[-1]
        answer += word

        if len(answer) < 3:
            answer += word

    return answer

# new_id = "z-+.^."
# print(solution(new_id))