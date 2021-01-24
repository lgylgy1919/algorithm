scoville = [0, 0, 1]
K = 7
answer = 0
while True:
    if min(scoville) < K and len(scoville) >= 2:
        a = scoville.pop(0)
        b = scoville.pop(0)
        c = a + b*2
        scoville.insert(0, c)
        scoville = sorted(scoville)
        answer += 1
    elif len(scoville) < 2:
        answer = -1
        break
    else:
        break

print(answer)
