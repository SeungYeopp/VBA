# 완주하지 못한 선수: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # dict 생성
    ans = {}
    # participant를 dict에 저장 후 value는 중복 인원 위해 값 증가
    for i in participant:
        ans[i] = ans.get(i, 0) + 1
    # completion의 인원을 key로 value 1씩 감소
    for j in completion:
        ans[j] -= 1
    # value가 남아있으면 key 반환(제너레이터 객체 사용 --> next() 사용하여 값 가져옴)
    return next(name for name in ans if ans[name])


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))