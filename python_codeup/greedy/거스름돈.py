change = int(input())
changes = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
kinds_n = 8
n = 0
while True:
    if (changes[kinds_n - 1]) > change:
        kinds_n -= 1
    else:
        change -= changes[kinds_n -1]
        n += 1
        if change == 0:
            break

print(n)
