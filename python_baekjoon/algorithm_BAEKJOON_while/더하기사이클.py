"""
import sys

n = int(sys.stdin.readline())
m = n
x = 0
while True:
    if int(m) < 10:
        a = str(m).zfill(2)
    else:
        a = str(m)
    arr = list(a)
    n_1 = int(arr[0]) + int(arr[1])
    n_2 = n_1 % 10
    n_3 = (int(arr[1]) * 10) + n_2
    if n_3 == n:
        x += 1
        break
    else:
        m = str(n_3)
        x += 1
print(x)

"""
"""
import sys

n = int(sys.stdin.readline())
m = n
x = 0
while True:
    a = ((m % 10) * 10) + (((m // 10) + (m % 10)) % 10)
    x += 1
    if n == a:
        print(x)
        break
    else:
        m = a
"""
import sys

n = int(sys.stdin.readline())
m = n
x = 0
while True:
    c, d = divmod(m, 10)
    a = (d * 10) + ((c + d) % 10)
    x += 1
    if n == a:
        print(x)
        break
    else:
        m = a
