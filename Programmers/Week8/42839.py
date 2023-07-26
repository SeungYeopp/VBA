# 소수 찾기: https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

# 주어진 수가 소수인지를 체크하는 함수
# 주어진 숫자의 약수는 제곱근 이하에서 나눠지는 값이 있는지를 확인해 해당 숫자가 소수인지 판별 가능
def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    ans = []
    num = []

    # 주어진 숫자로 만들 수 있는 모든 조합을 구함
    for i in range(1, len(numbers) + 1):
        # permutation 함수를 사용하여 조합 생성 및 ''.join() 함수를 사용하여 문자열로 조합 생성
        num = list(map(''.join, permutations(numbers, i)))

        # 각 조합을 정수로 변환하여 소수인지 체크하고, 소수일 경우 ans 리스트에 추가
        for n in num:
            if checkPrime(int(n)):
                ans.append(int(n))
    # 중복을 제거한 소수의 개수를 반환
    return len(set(ans))


print(solution("17"))
print(solution("011"))
