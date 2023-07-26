# 피로도: https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    ans = -1

    # 모든 던전의 순열을 구함
    for dungeons_list in permutations(dungeons, len(dungeons)):
        cnt = 0
        cur_t = k
        # 각 던전에 대해서 플레이어의 피로도가 최소 필요 피로도보다 크거나 같을 때
        # 피로도를 소모하며 던전 수 count + 1
        for t, t_consume in dungeons_list:
            if cur_t >= t:
                cur_t -= t_consume
                cnt += 1
        ans = max(ans, cnt)

    # 탐험 가능한 최대 던전 수 반환
    return ans



print(solution(80, [[80,20],[50,40],[30,10]]))
