import sys

arr = []
for i in range(9):
    n = int(sys.stdin.readline())
    arr.append(n)

print(max(arr))
print(arr.index(max(arr)) + 1)
