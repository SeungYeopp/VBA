# K번째 수: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    # commands의 각 항목에 따라 array를 slicing 하여 정렬 후 cmd[2] - 1번 째 원소를 선택 후 선택된 값을 리스트로 만들어 반환
    return list(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1] for cmd in commands)


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
