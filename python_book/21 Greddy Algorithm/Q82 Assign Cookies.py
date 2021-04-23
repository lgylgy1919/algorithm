import bisect

"""
children = [7, 8, 9, 10]
cookies = [5, 6, 7, 8]
"""
children = [1, 2]
cookies = [1, 2, 3]

g = [7, 8, 9, 10]
s = [5, 6, 7, 8]


def findContentChildren1(children, cookies):

    result = 0
    children.sort()
    cookies.sort()
    for cookie in cookies:
        if cookie >= children[0]:
            children.pop(0)
            result += 1
        if not children:
            break

    return result


def findContentChildren2(g, s):
    g.sort()
    s.sort()

    child_i = cookie_j = 0
    # 만족하지 못할 때까지 그리디 진행
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[cookie_i]:
            child_i += 1
        cookie_j += 1

    return child_i


def findContentChildren3(g, s):
    g.sort()
    s.sort()

    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    print(result)
    return result


findContentChildren3(g, s)
