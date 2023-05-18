# 주식가격: https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    # 결과 저장 리스트 0으로 초기화
    ans = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            # 가격이 떨어지지 않은 기간 1초 증가
            ans[i] += 1
            # 현재 가격이 이후 가격 보다 높다면 break
            if prices[i] > prices[j]:
                break

    return ans


print(solution([1, 2, 3, 2, 3]))