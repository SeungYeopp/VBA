# 가장 큰 수: https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    # 주어진 숫자 배열을 문자열로 교체
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    ans = ''.join(numbers)
    if ans[0] == '0':
        return '0'
    return ans


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
