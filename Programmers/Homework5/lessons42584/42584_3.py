# 주식가격: https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    ans = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고 현재 가격이 stack의 top에 해당하는 시점의 가격보다 낮다면(가격이 떨어졌다면)
        while stack and price < prices[stack[-1]]:
            # 스택에 가장 최근데 추가된 idx pop 후 j에 저장
            j = stack.pop()
            # 현재 시점에서 가격이 떨어지기 시작한 시점 j 빼서(가격이 떨어지지 않은 기간) ans[j]에 저장
            ans[j] = i - j
        # 현재시점을 스택에 append
        stack.append(i)


    # 스택에 남아있는 요소에 대해
    while stack:
        j = stack.pop()
        # 떨어지지 않은 기간을 계산하여 ans에 저장
        ans[j] = len(prices) - 1 - j

    return ans


print(solution([1, 2, 3, 2, 3]))