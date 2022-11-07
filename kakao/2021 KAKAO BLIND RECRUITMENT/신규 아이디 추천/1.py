'''

명세에 맞추어서 구현하는 문제
시간 복잡도는 O(n) 이나 re 라이브러리가 시간 먹음

'''



import sys, re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id[-1] == '.':
            new_id = new_id[:-1]
    if new_id:
        string = new_id[-1]
        size = 3-len(new_id)
        if size <= 2:
            new_id = new_id + string * size
    answer = new_id
    return answer