import collections
from functools import reduce


def solution(c):
    return reduce(lambda x, y: x*y, [a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
