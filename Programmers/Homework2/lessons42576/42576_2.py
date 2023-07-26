# 완주하지 못한 선수: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))