participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(1)
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            print(participant[i])
            return participant[i]


solution(participant, completion)
