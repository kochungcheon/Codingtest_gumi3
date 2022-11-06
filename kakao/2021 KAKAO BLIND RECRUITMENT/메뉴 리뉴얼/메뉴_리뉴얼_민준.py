from itertools import combinations

'''
1. 2명 이상의 손님이 2번 이상 시킨 단품 메뉴 조합만이 코스요리가 될 자격이 생긴다.
2. 가능한 조합과 그 조합의 호출 횟수를 저장할 dict를 만들어준다.
'''

def solution(orders, course):
    answer = []
    for number in course:                            # 단품 메뉴가 (number)개 포함 된 코스요리를 만든다.
        setmenu_dict = dict()                        # setmenu_dict = { 세트메뉴 종류 : 세트메뉴 수 } 형태로 저장할 dict 만들어줌.
        for menu in orders:
            menu = sorted(menu)                      # 조합 만들기 전 테스트 3에 "WXA" 처럼 순서 정렬 안된 메뉴 있어서 sort 해줘야함.
            for comb in combinations(menu, number):
                ## 1. tuple을 문자열로 바꾸기!
                setmenu = ""
                for a in comb:
                    setmenu += a
                if setmenu in setmenu_dict:          # 이미 setmenu가 dict안에 있다면 value += 1
                    setmenu_dict[setmenu] += 1
                else:
                    setmenu_dict[setmenu] = 1        # 없다면 value = 1

        # 같은 갯수의 단품 요리 조합일 때마다 손님이 조합한 횟수가 같은 것들만 정답 리스트에 넣어줘야 한다.
        if len(setmenu_dict) != 0:
            needs = max(setmenu_dict.values())       # 손님이 조합한 횟수의 최댓값
        for key, value in setmenu_dict.items():
            if needs >= 2 and value == needs:        # 손님들이 2번 이상 조합했고 and 최댓값이면
                answer.append(key)                   # key값(setmenu)를 answer에 append한다.

    answer.sort()  # 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# print(solution(orders, course))

