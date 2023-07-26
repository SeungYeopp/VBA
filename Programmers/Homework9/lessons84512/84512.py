# 모음사전: https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product

def solution(word):

    target = ['A', 'E', 'I', 'O', 'U']
    arr = []

    # itertools.product()를 통해 중복순열을 수행하여 arr 리스트에 추가
    for i in range(1, len(target) + 1):
        arr += list(map("".join, product(target, repeat=i)))

    # 오름차순 정렬
    arr.sort()

    # 값 확인하여 word와 같을 경우 인덱스 번호 + 1 반환
    for idx in range(len(arr)):
        if arr[idx] == word:
            return idx + 1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
