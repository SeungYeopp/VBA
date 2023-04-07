# 완주하지 못한 선수: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    for item in completion:
        participant.remove(item)
    return participant[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))