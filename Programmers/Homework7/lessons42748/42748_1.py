# K번째 수: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    ans = []
    for cmd in commands:
        # array를 slicing 하여 정렬 후 cmd[2] - 1번 째 원소를 선택하여 ans 리스트에 append
        ans.append(list(sorted(array[cmd[0]-1:cmd[1]]))[cmd[2]-1])
    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
