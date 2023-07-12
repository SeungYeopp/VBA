# 모의고사: https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # 수포자 패턴 초기화
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    # 맞힌 문제 수 0 초기화
    score = [0 for _ in range(len(students))]

    # 주어진 문제 전부 채점
    for idx, answer in enumerate(answers):
        for i, student in enumerate(students):
            if answer == student[idx % len(student)]:
                score[i] += 1

    # 가장 많은 점수를 득점한 학생을 뽑은 후 값 반환
    return list(idx + 1 for idx, s in enumerate(score) if s == max(score))


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
