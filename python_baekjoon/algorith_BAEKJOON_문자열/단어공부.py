w = input().upper()
arr = []
new_w = []
while True:
    arr.append(w.count(w[0]))
    new_w.append(w[0])
    w = w.replace(w[0], "")
    if len(w) < 1:
        break
m = max(arr)
if arr.count(m) == 1:
    idx = arr.index(m)
    print(new_w[idx])
else:
    print("?")
