# K번째 수: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    # map 함수는 첫번 째 인자로 함수를, 두번째 인자로 반복 가능한 객체를 받아, 반복 가능한 객체의 각 요소에 함수를 적용한 결과를 반환
    # commands의 각 항목에 따라 array를 slicing 하여 정렬 후 cmd[2] - 1번 째 원소를 선택 후 선택된 값을 리스트로 만들어 반환
    return list(map(lambda cmd: sorted(array[cmd[0] - 1: cmd[1]])[cmd[2] - 1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
