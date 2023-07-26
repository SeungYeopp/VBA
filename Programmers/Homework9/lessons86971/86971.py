# 전력망을 둘로 나누기: https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def bfs(start, graph, check_link):
    # 방문 여부 기록 배열
    visited = [False] * len(graph)
    # 시작 노드를 queue에 추가
    queue = deque([start])
    # 시작 노드 방문
    visited[start] = True
    cnt = 1

    # queue가 비어있지 않는 동안 반복
    while queue:
        v = queue.popleft()

        # 꺼낸 노드의 인접 노드를 방문
        # 방문하지 않았고, 간선이 끊어진 것이 아니라면
        # visited --> True 변경 / 방문할 노드 queue에 추가 / cnt + 1
        for adj_v in graph[v]:
            if not visited[adj_v] and check_link[v][adj_v]:
                visited[adj_v] = True
                queue.append(adj_v)
                cnt += 1

    return cnt


def solution(n, wires):
    ans = float('inf')

    # 간선 연결 여부 저장 2차원 배열
    check_link = [[True]*(n+1) for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]

    # 그래프 구성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 모든 간선에 대해
    # 간선을 끊은 후 BFS 수행.
    # 두 트리의 노드 개수 차이의 절대값의 최솟값 구함
    for a, b in wires:
        check_link[a][b] = check_link[b][a] = False
        cnt_a = bfs(a, graph, check_link)
        cnt_b = bfs(b, graph, check_link)
        ans = min(ans, abs(cnt_a - cnt_b))

        # 끊었던 간선 다시 연결
        check_link[a][b] = check_link[b][a] = True

    return ans


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
