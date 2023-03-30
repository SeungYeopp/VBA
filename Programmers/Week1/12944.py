# 평균 구하기 : https://school.programmers.co.kr/learn/courses/30/lessons/12944
def solution(arr):
    answer = 0
    answer = sum(arr) # 배열의 합을 answer 에 저장

    return answer/len(arr) # 평균 구하기


print(solution(arr=[1, 2, 3, 4]))
print(solution(arr=[5, 5]))
