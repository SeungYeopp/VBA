# 짝수와 홀수 : https://school.programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    answer = ''
    if (num % 2):  # num이 홀수일 때
        return 'Odd'
    else:  # num이 짝수일 때
        return 'Even'


print(solution(3))
print(solution(4))
