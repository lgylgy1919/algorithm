import collections

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer)[0])


solution(participant, completion)
