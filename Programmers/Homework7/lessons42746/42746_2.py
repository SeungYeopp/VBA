# 가장 큰 수: https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key


def solution(numbers):
    # 주어진 숫자 배열을 문자열로 교체
    numbers = list(map(str, numbers))
    # 인자 두개를 받아 정렬 함수의 조건에 의해 0보다 작으면 위치를 바꿈 + 내림차순으로 정렬
    numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
    # 예외 케이스(0 반복) 제거 후 정답 반환
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
