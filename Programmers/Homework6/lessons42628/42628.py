# 이중우선순위큐: https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq as hp


def solution(operations):
    heap = []

    for operation in operations:
        # 연산과 연산자 구분
        op, operand = operation.split(' ')
        operand = int(operand)

        # I 연산이면 heap에 값 추가
        if op == 'I':
            hp.heappush(heap, operand)
        # D 연산이며, 힙이 비어있지 않을 때, operand가 음수면 가장 작은 값, 양수면 가장 큰 값 제거
        elif heap:
            if operand < 0:
                hp.heappop(heap)
            else:
                heap.remove(max(heap))

        # heapify를 통해 heap 재정렬
        hp.heapify(heap)

    # 힙이 비어있다면 [0, 0] 반환
    if not heap:
        return [0, 0]
    # 힙이 비어있지 않다면 힙에서 가장 큰 값과 가장 작은 값 리스트로 반환
    return [max(heap), heap[0]]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))