m = int(input())
n = 1
while True:
    if m == 1:
        print(1)
        break
    elif m <= (3 * n * (n + 1) + 1):
        print(n + 1)
        break
    else:
        n += 1
