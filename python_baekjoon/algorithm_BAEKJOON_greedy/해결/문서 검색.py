arr = input()
index = input()
x = 0
while True:
    if index in arr:
        arr = arr.replace(index, "*", 1)
        x += 1
    else:
        break
print(x)
