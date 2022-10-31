'''
n을 k진수로 변환하고 변환할 k진수안에 정해진 조건에 맞는 소수를 구하는게 목표였다.
1. n을 k진수로 변환하고
2. 단, 소수가 맞더라도 문제의 조건에 알맞는 소수인지 판별해야 했다.
'''

# n을 k진수로 변환하는 함수
def n_to_k(n, k):
    string = ''
    while n:
        string += str(n%k)
        n //= k
    return string[::-1]

# 소수를 판별하는 함수
def prime_num(n):
    n = int(n)
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 문제의 조건에 알맞는지 확인하는 함수
def solution(n, k):
    conv_num = n_to_k(n,k)
    count = 0
    for j in conv_num.split('0'):
        if not j:
            continue
        if prime_num(j):
            count += 1
    return count