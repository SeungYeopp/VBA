# 카펫: https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    # yellow = height * width
    # brown = 2*(height + width) + 4
    # height + width = (brown - 4) // 2

    # yellow 의 가로 세로 길이를 width, height로 설정 후 width + height 값을 total에 저장
    total = (brown - 4) // 2
    width = 0

    for w in range(total):
        # 반복문을 돌며 w * (total-w) == yellow인 값 확인 후 max값을 width에 저장
        if w * (total - w) == yellow:
            width = max(w, total - w)
            break

    # 전체 카펫의 가로, 세로 길이는 yellow의 가로 길이 + 2, 세로 길이 + 2.
    return [width + 2, total - width + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
