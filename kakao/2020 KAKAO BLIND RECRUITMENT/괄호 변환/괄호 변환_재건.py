'''
문제 솔직히 이해 안감
그러나 요구사항을 구현하는 것 외에 다른 고려사항은 없어보여서 문제에서 주어진 내용대로 구현
O(N)
'''


from collections import deque


def is_right(p):
    stack = [p[0]]
    for i in range(1, len(p)):
        if p[i] == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


def solution(p):
    if p == '':
        return ''
    ss = p[0]
    cnt = 1
    for i in range(1, len(p)):
        if p[i] == p[0]:
            cnt += 1
        else:
            cnt -= 1
        ss += p[i]
        if cnt == 0:
            u = ss
            if p[i+1:]:
                v = p[i+1:]
            else:
                v = ''
            break
    if is_right(u):
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        u = deque(u)
        u.pop()
        u.popleft()
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        u = ''.join(u)
        return tmp + u


print(solution("()))((()"))
print(solution("(()())()"))
