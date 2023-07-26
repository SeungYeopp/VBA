# 폰켓몬 : https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # 배열의 길이의 절반을 N에 저장
    N = len(nums) // 2
    # 배열을 집합으로 형 변환 ==> 중복 제거
    nums_set = set(nums)
    # 집합의 크기가 가져갈 수 있는 종류의 수보다 많으면 N 반환 아니면 집합의 크기 반환
    return (N if len(nums_set) >= N else len(nums_set))


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
