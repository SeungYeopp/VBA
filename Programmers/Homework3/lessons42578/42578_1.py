# 의상: https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    # 옷 종류를 저장할 딕셔너리 생성
    clothes_dict = {}

    # 옷의 종류를 딕셔너리의 key에 저장하고, 갯수 counting
    for _, cl_type in clothes:
        if cl_type not in clothes_dict:
            clothes_dict[cl_type] = 1
        else:
            clothes_dict[cl_type] += 1

    ans = 1

    # 딕셔너리의 각 값에 대해 반복
    for val in clothes_dict.values():
        # 해당 종류의 옷을 입지 않는 경우도 존재하기 때문에 val + 1
        ans *= (val + 1)

    # 모두 입지 않았을 경우를 제외하여야하기 때문에 ans - 1
    return ans - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
