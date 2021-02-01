s = ["h", "e", "l", "l", "o"]

# 투 포인터를 활용한 스왑


def reverseString_twoPointer(s) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬다운 방식


def reverseString_python(s) -> None:
    s.reverse()


reverseString_twoPointer(s)
print(s)
reverseString_python(s)
print(s)
