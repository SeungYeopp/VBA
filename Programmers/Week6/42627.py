# 디스크 컨트롤러: https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq as hq


def solution(jobs):
    # (소요시간, 시점) 순으로 reverse로 정렬
    tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    queue = []
    # tasks에서 꺼내서 queue에 저장
    hq.heappush(queue, tasks.pop())

    # 현재 시간과 총 소요시간 초기화
    cur_time, total_time = 0, 0
    while len(queue) > 0:
        # Priority Queue에서 작업을 pop한 후 현재시간 업데이트 및 총 소요시간 계산
        duration, start_point = hq.heappop(queue)
        cur_time = max(cur_time + duration, start_point + duration)
        total_time += cur_time - start_point

        # 현재시간 이전에 도착하는 모든 작업을 queue에 추가
        while len(tasks) > 0 and tasks[-1][1] <= cur_time:
            hq.heappush(queue, tasks.pop())

        # 만약 tasks에 작업이 남아있고, queue가 비어있다면, tasks에서 작업을 pop한 후 queue에 추가
        if len(tasks) > 0 and len(queue) == 0:
            hq.heappush(queue, tasks.pop())

    # 평균 소요시간 계산
    return total_time // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
