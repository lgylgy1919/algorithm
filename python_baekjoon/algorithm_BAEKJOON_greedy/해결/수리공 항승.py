n, l = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()
x = 0
k = 0
for i in range(n - 1):
    m = arr[i + 1] - arr[i]
    k += m
    if (k + 1) > l:
        x += 1
        k = 0
print(x + 1)
