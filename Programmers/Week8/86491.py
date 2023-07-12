# 최소 직사각형: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # sizes 내 각 숫자 쌍에 대해, 쌍의 최대 값을 widths list에, 최소 값을 heights list에 추가
    widths = list(max(size) for size in sizes)
    heights = list(min(size) for size in sizes)

    # 최대 너비와 최대 높이를 곱하여 최대면적 반환
    return max(widths) * max(heights)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
