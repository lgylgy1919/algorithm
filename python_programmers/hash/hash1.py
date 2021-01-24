participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
'''
return = "mislav"
'''


def solution(participant, completion):
    for name in completion:
        participant.remove(name)
    answer = participant[0]
    print(answer)
    return answer


solution(participant, completion)
