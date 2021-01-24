import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = max(arr)
print(m)

sum = 0
for i in range(n):
    s = (arr[i] / m) * 100
    sum += s
print(sum / n)
