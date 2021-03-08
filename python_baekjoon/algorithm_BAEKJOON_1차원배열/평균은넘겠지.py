import sys

n = int(sys.stdin.readline())
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    avg = sum(arr[j] for j in range(1, len(arr))) / arr[0]
    a = 0
    for j in range(1, len(arr)):
        if arr[j] > avg:
            a += 1
    result = str("%0.3f" % ((a / arr[0]) * 100))
    print(result + "%")

