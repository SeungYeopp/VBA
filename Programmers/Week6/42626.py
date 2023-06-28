# 더 맵게: https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville) # 리스트를 minHeap으로 변환
    ans = 0

    while True:
        min1 = hq.heappop(scoville) # 힙에서 가장 낮은 변수 추출

        if min1 >= K: # min1이 K 이상일 경우 break
            break
        if len(scoville) == 0: # 힙에 남아 있는 요소가 없을 경우 return -1
            return -1

        min2 = hq.heappop(scoville) # 힙에서 두번 째로 낮은 변수 추출
        hq.heappush(scoville, min1 + min2 * 2) # 계산 후 heap에 삽입
        ans += 1 # ans에 1 증가

    return ans


print(solution([1, 2, 3, 9, 10, 12], 7))
