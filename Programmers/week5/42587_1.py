# 프로세스: https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    ans = 0
    queue = list(enumerate(priorities))
    priorities.sort(reverse=True)  # 우선순위를 높은 순으로 정렬

    while True:

        idx, p = queue.pop(0)  # 첫 번째 문서 pop
        # 만약 첫 번째 문서가 가장 높은 우선 순위라면, 현재까지 출력한 작업 수 +1
        if priorities[0] == p:
            ans += 1
            # 우선순위 리스트에서 해당 문서 pop
            priorities.pop(0)
            # idx가 location과 같다면 현재까지 출력한 작업 수 반환
            if idx == location:
                return ans
        else:
            queue.append((idx, p))  # 아니라면 문서를 큐의 끝에 추가


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
