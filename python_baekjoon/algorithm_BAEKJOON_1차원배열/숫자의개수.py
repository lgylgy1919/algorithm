# import sys

# m = 1
# for i in range(3):
#     n = int(sys.stdin.readline())
#     m *= n
# arr = list(map(int, str(m)))

# for j in range(10):
#     print(arr.count(j))

cnt = [0 for _ in range(10)]
A, B, C = (int(input()), int(input()), int(input()))
for c in str(A * B * C):
    cnt[ord(c) - ord("0")] += 1
[print(x) for x in cnt]
