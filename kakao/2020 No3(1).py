gems = ["A", "A", "B"]

l_point = 0
r_point = len(gems)

new_gems = len(list(set(gems)))


while True:
    sub_gems = len(list(set(gems[l_point:r_point])))
    if sub_gems == new_gems:
        r_point -= 1
    else:
        r_point += 1
        break

while True:
    sub_gems = len(list(set(gems[l_point:r_point])))
    if sub_gems == new_gems:
        l_point += 1
    else:
        l_point -= 1
        break


print(l_point + 1, r_point)
