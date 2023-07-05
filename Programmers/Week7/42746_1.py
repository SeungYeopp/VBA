# 가장 큰 수: https://school.programmers.co.kr/learn/courses/30/lessons/42746
# timeout
from itertools import permutations


def solution(numbers):
    # 문자열로 바꾼 뒤 순열을 통해 모든 조합을 만들어낸 뒤 이를 합한 값 중 가장 큰 값을 구함
    return max(list(map(''.join, permutations([str(x) for x in numbers]))))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
