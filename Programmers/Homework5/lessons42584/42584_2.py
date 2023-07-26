# 주식가격: https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque


def solution(prices):
    # 결과 반환 리스트 초기화
    ans = [0] * len(prices)
    # prices를 deque으로 변환
    prices = deque(prices)

    for i in range(len(ans)):
        price = prices.popleft()
        for _, next_price in enumerate(prices):
            # 가격이 떨어지지 않은 기간 1초 증가
            ans[i] += 1
            # 현재 가격이 이후 가격 보다 높다면 break
            if price > next_price:
                break

    return ans


print(solution([1, 2, 3, 2, 3]))