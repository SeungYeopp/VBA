# 다리를 지나는 트럭: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# timeout
def solution(bridge_length, weight, truck_weights):
    ans = 0
    bridge = [0] * bridge_length

    while len(truck_weights):
        ans += 1 # 시간 증가
        bridge.pop(0) # 다리를 지난 트럭은 제거
        if sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights.pop(0))
    ans += bridge_length # 마지막 트럭이 다리를 지나는 시간 추가
    return ans


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))