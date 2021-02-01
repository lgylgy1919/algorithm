import collections
import re
from collections import deque
s = "A man, a plan, a canal: Panama"


# 리스트 풀이 법
def isPalindrome_list(s) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


answer = isPalindrome_list(s)
print(answer)


# 데크 풀이법


def isPalindrome_deque(s) -> bool:
    strs: deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


answer = isPalindrome_deque(s)
print(answer)


# 슬라이싱 사용


def isPalindrome_slicing(s) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


answer = isPalindrome_slicing(s)
print(answer)
