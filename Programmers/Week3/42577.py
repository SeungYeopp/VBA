# 전화번호 목록: https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # 전화번호를 저장할 딕셔너리 생성
    phone_dict = {}

    # 전화번호부의 각 전화번호를 딕셔너리의 키로 저장
    for key in phone_book:
        phone_dict[key] = True

    for phone_num in phone_dict:
        tmp = ''

        # 전화번호의 각 숫자에 대해 반복
        for num in phone_num:
            tmp += num
            # 임시 문자열이 딕셔너리에 있고, 원래 전화번호와 다르면(접두어 O)
            if tmp in phone_dict and tmp != phone_num:
                return False

    # 접두어 X
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
