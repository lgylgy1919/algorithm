ass = [3, 3, 2, 1, 2]
ans = 0
while True:
    for i in range(0, len(ass) - 1):
        for j in range(i + 1, len(ass)):
            if ass[i] < ass[j]:
                ass[i], ass[j] = ass[j], ass[i]
                print(ass[i], ass[j])
                ans += 1
print(ans)
