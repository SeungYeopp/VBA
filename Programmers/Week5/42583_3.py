# 다리를 지나는 트럭: https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    ans = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0  # 다리 위의 트럭 무게 합
    trucks = deque(truck_weights)

    while trucks:
        ans += 1
        bridge_weight -= bridge.popleft()  # 다리의 왼쪽(먼저 들어온) 트럭을 제거

        # 새로운 트럭이 다리 위에 올라갈 수 있는지 확인
        if bridge_weight + trucks[0] <= weight:
            truck = trucks.popleft()  # 대기 중인 트럭 중 첫 번째 트럭을 꺼냄
            bridge.append(truck)  # 다리 위에 트럭을 추가
            bridge_weight += truck  # 다리 위의 트럭 무게 합 갱신
        else:
            bridge.append(0)  # 트럭이 올라갈 수 없는 경우, 다리를 이동

    # 마지막 트럭이 다리를 건너는 데 걸리는 시간을 더함
    ans += bridge_length

    return ans


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
