# x만큼 간격이 있는 n개의 숫자 : https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    # i가 1부터 n까지 x * i 값을 리스트로 저장
    answer = [x * i for i in range(1, n + 1)]
    return answer


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))