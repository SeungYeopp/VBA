# 올바른 괄호: https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    # 괄호를 저장할 스택 초기화
    stack = []
    for c in s:
        # 현재 괄호가 "("이면 스택에 추가
        if c == '(':
            stack.append(c)
        else:
            # 현재 문자가 ")"이면 스택의 마지막 원소 pop
            if stack:
                stack.pop()
            # stack이 비어있으면 return false
            else:
                return False

    # 반복문이 끝난 후 스택이 비어있다면 True, 아니면 return False
    return len(stack) == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))