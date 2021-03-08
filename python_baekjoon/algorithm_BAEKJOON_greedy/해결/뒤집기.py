arr = input()
l = len(arr)
k = 0
for i in range((l - 1)):
    if arr[i] != arr[i + 1]:
        k += 1
if k % 2 == 0:
    print(int(k / 2))
else:
    print(int((k + 1) / 2))
