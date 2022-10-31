# 1
def num_change(a, b):
    k_num = ''
    while a > 0:
        a, x = divmod(a, b)
        k_num += str(x)
    return str(k_num[::-1])


# 2
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


# 3
def solution(n, k):
    ans = 0
    for num in num_change(n, k).split('0'):
        if num != "":
            if prime(int(num)):
                ans += 1
    return ans


'''
두개의 함수를 추가로 작성하였다.
1. 진법 변환 함수. divmod는 몫과 나머지를 출력해주는 내장함수이다. // 와 %를 쓰는 과정에서
a 값을 갱신하는 과정에서 문제가 발생하여 사용하였다.
2. 소수를 판별하는 함수이다. 2부터 판단할 숫자의 제곱근까지만 판단해주면 되기에 (곱센 연산시 연산의 대칭성)
int(n**2)를 사용하여 제곱근을 구해주었다.
3. 숫자 리스트를 진법변환을 해주어 분리를 해준뒤 소수 판별을 하여, 계산을 넣어주었다.
if num != "": 을 통해 000상황에서 0이 세려져서 빈 문자열이 반환되는 경우를 제거 해주었다.
'''
'''
O(Nlog(M))
'''