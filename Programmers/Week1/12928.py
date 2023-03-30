# 약수의 합 : https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    # 1부터 n까지 n을 i로 나눴을 때 나머지가 0이면 값을 계속 더함
    answer = sum([i for i in range(1, n + 1) if n % i == 0])
    return answer


print(solution(12))
print(solution(5))
