# 나머지가 1이 되는 수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    for i in range(1, n):
        # n을 i로 나눈 나머지가 1일 때 값 반환
        if n % i == 1:
            return i


print(solution(10))
print(solution(12))