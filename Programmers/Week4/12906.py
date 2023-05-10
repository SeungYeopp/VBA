# 같은 숫자는 싫어: https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    # arr의 첫번째 원소를 ans 리스트에 추가
    ans = [arr[0]]

    # arr의 모든 원소에 대해 반복
    for num in arr:
        # 현재 num이 ans의 마지막 원소와 같다면 중복이기 때문에 continue
        if num == ans[-1]:
            continue

        # 중복되지 않은 경우, ans에 원소 추가
        ans.append(num)

    return ans


print(solution([1,1,3,3,0,1,1]))