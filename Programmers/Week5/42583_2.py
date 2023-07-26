# 다리를 지나는 트럭: https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    ans = 0
    bridge = [0] * bridge_length
    bridge_weight = 0  # 다리 위의 트럭 무게 합

    while truck_weights:
        ans += 1  # 시간 증가
        bridge_weight -= bridge.pop(0)  # 다리를 지난 트럭은 제거

        # 다리 위의 트럭 무게와 다음 트럭의 무게 합이 weight 이하일 경우
        if bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)  # 다음 트럭
            bridge.append(truck)  # 트럭을 다리에 추가
            bridge_weight += truck  # 다리 위의 트럭 무게 합 업데이트
        else:
            bridge.append(0)  # 다음 트럭이 다리에 올라갈 수 없는 경우, 무게 0을 추가

    ans += bridge_length  # 마지막 트럭이 다리를 지나는 시간 추가
    return ans


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))