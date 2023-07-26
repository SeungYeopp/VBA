# 문자열 내 p와 y의 개수 : https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    answer = True
    # 입력 문자열 s를 소문자로 변환 후 p와 y의 수가 같으면 True 반환
    if s.lower().count("p") == s.lower().count("y"):
        return True
    else:
        return False


print(solution("pPoooyY"))
print(solution("Pyy"))
