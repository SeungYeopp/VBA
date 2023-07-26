# 의상: https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import Counter


def solution(clothes):
    ans = 1

    # 옷 리스트에서 옷 종류를 추출하여 Counter 객체 생성
    clothes_type = Counter(cl_type for _, cl_type in clothes)

    # Counter 객체의 각 값에 대해 반복
    for val in clothes_type.values():
        # 해당 옷 종류를 입지 않는 경우를 고려하여 val + 1을 곱함
        ans *= (val+1)

    # 아무것도 입지 않는 경우 제외
    return ans-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
