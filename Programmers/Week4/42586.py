# 기능개발: https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    count = 0
    time = 0

    # 모든 프로젝트가 완료될 때까지
    while len(progresses) > 0:

        # 첫번째 프로젝트가 완료되었거나 시간 * 작업 속도를 곱한 값이 100%를 넘을 경우
        if (progresses[0]+speeds[0]*time >= 100):
            # progresses, speeds의 첫번째 원소 pop, count 1 증가
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        # 첫번째 프로젝트가 완료되지 않았을 경우
        else:
            # 현재까지 완료된 프로젝트의 수 answer에 append 후 count 0으로 초기화
            if count > 0:
                answer.append(count)
                count = 0
            # 시간 1 증가
            time += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))