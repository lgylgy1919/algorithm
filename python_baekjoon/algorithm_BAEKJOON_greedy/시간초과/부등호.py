"""
n = int(input())
ineq = list(input().split(" "))
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
from itertools import permutations

can = list(permutations(number, len(ineq)))
tt = []
for i in range(len(ineq)):
    if ineq[i] == "<":
        tt.append("a")
    else:
        tt.append("b")
last_can = []
for j in can:
    bb = []
    for i in range(len(j) - 1):
        if j[i] < j[i + 1]:
            bb.append("a")
        else:
            bb.append("b")
    if j[len(j) - 1] > j[len(j) - 2]:
        bb.append("a")
    else:
        bb.append("b")
    if bb == tt:
        last_can.append(j)

l = len(last_can)
for i in range(len(ineq)):
    print(last_can[l - 1][i], end="")
print()
for i in range(len(ineq)):
    print(last_can[0][i], end="")

"""
# 블로그 풀이
n = int(input())
op = input().split()
c = [False] * 10
print(c)
mx, mn = "", ""


def possible(i, j, k):
    if k == "<":
        return i < j
    if k == ">":
        return i > j
    return True


def solve(cnt, s):
    global mx, mn
    if cnt == n + 1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]):
                c[i] = True
                solve(cnt + 1, s + str(i))
                c[i] = False


solve(0, "")
print(mx)
print(mn)
