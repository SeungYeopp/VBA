# 프로세스: https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    ans = 0

    # priorities를 enumerate하여 작업의 위치와 우선순위를 함께 저장하는 큐를 생성
    queue = deque(enumerate(priorities))

    # 큐가 빌때까지 반복
    while queue:
        # 큐의 가장 앞에 있는 작업 pop
        tmp = queue.popleft()
        # 만약 큐에 다른 작업이 남아있고, 그 중 우선순위가 더 높은 작업이 존재한다면
        if queue and max(queue, key=lambda tup: tup[1])[1] > tmp[1]:
            queue.append(tmp) # 큐에 append
        else:
            # 현재 출력한 작업 + 1
            ans += 1
            # idx가 location과 같다면 현재까지 출력한 작업 수 반환
            if tmp[0] == location:
                return ans


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
