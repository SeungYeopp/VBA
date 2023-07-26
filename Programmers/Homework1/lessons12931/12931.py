# 자릿수 더하기 : https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    # n != 0
    while n:
        # n을 10으로 나눈 나머지를 answer에 더함
        answer += (n % 10)
        # n을 10으로 나눈 몫을 n에 저장
        n //= 10

    return answer


print(solution(123))
print(solution(987))
