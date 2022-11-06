def solution(new_id):

    new_id = new_id.lower()

    ans = ''

    for word in new_id:
        if word.isalpha() or word.isdigit() or word =='-' or word =='-' or word =='_' or word == '.':
            ans += word
    flag = 1
    while flag:
        if '..' in ans:
            ans = ans.replace('..', '.')
        else:
            flag = 0

    ans = ans.strip('.')

    if not ans:
        ans += 'a'

    if len(ans) >= 16:
        ans = ans[:15]
        ans = ans.rstrip('.')

    flag = 1
    if len(ans) <= 2:
        tmp = ans[-1]
        while flag:
            ans += tmp
            if len(ans) == 3:
                flag = 0

    return ans

# 명세 순서대로 순서대로 진행
# 오랜만에 strip 사용