# H-Index: https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        # 현재 인덱스가 논문 인용 숫자보다 커지게 되는 시점이 H-index의 최대
        if idx >= citation:
            return idx

    return len(citations)


print(solution([3, 0, 6, 1, 5]))
