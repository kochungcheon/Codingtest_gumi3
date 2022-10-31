'''

시간 복잡도는 NlogN
정해진 숫자를 정해진 지수로 변환
에라토스테네스 체를 응용해서 소수 판별 ( 에라토스테네스체 리스트로 구현해서 사용하면 시간 터짐)
0을 기준으로 소수 판별
'''





def change_number(n, k): # 진수변환
    tmp = ""
    while n > 0:
        tmp += str(n % k)
        n = n // k
    return ''.join(reversed(tmp))

def solution(n, k):
    answer = 0
    k_num = change_number(n, k)
    for n in k_num.split('0'):
        if n == "": continue # 연속되는 0 처리
        if is_prime(int(n)):
            answer += 1
    return answer

def is_prime(n):
    if n == 1: return False
    if n == 2 or n == 3: return True
    tmp = 1
    for i in range(2, int(n**(0.5)+1), tmp):
        if n % i == 0:
            return False
        tmp = i
    return True

