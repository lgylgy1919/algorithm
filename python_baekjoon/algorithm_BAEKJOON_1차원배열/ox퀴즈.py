"""
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    score = 0
    arr = list(sys.stdin.readline())
    m = 0
    for i in range(len(arr)):
        if arr[i] == "O":
            m += 1
            score += m
        else:
            m = 0
    print(score)
"""

N = int(input())
for _ in range(N):
    print(sum([int(len(x) * (len(x) + 1) / 2) for x in input().split("X")]))

