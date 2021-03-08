n = 1

answer = 0

while True:
    if n == 1:
        break
    if answer > 500:
        answer = -1
        break
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    answer += 1


print(answer)
