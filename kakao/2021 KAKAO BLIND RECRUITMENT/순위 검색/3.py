'''
조건에 맞는 것을 찾고
몇개인지 파악하는 문제 단 효율성 때문에 이진탐색을 통해 개수 체크를 했어야 했다.
bisect 사용 하는 것을 연습해야한다. O(nlogn)


'''




from itertools import combinations


def solution(info, query):
    ans = []
    data = {}
    for person in info:
        x = person.split(' ')
        score = int(x[-1])
        conditions = x[:-1]
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if(changed_t_c in data):
                    data[changed_t_c].append(score)
                else:
                    data[changed_t_c] = [score]
    for value in data.values():
        value.sort()
    for q in query:
        x = [i for i in q.split() if i != 'and']
        x_score = int(x[-1])
        cmd = '/'.join(x[:-1])
        if cmd in data:
            value = data[cmd]
            if len(value) > 0:
                s, e = 0, len(value)
            while s != e and s != len(value):
                if x_score <= value[(s+e)//2]:
                    end = (s + e)//2
                else:
                    start = (s+e)//2 + 1
            ans.append(len(value)-s)
        else:
            ans.append(0)

    return ans