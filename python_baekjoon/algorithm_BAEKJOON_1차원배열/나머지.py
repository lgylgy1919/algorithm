import sys

arr = []
for _ in range(10):
    a = int(sys.stdin.readline())
    arr.append(a % 42)

print(len(set(arr)))
