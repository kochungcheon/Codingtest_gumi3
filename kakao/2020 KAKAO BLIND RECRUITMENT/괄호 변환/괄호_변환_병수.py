def divide(p):
    start = 0
    end = 0

    for i in range(len(p)):
        if p[i] == '(':
            start += 1
        else:
            end += 1
        if start == end:
            return p[:i + 1], p[i + 1:]


def check(u):
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    # 1
    if not p:
        return ""
    # 2
    u, v = divide(p)
    # 3
    if check(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1~3
        answer = '('
        answer += solution(v)
        answer += ')'
        # 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        # 4-5
        return answer