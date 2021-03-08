genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
ids = []
for i in range(len(genres)):
    ids.append(i)

answer = []

lists = list(zip(genres, plays, ids))
new_lists = sorted(lists, key=lambda x: (x[0], -x[1]))

diction = {}
for genre in new_lists:
    if genre[0] in diction:
        a += int(genre[1])
        diction[genre[0]] = a
    else:
        diction[genre[0]] = int(genre[1])
        a = int(genre[1])


new_diction = sorted(diction.items(), key=lambda x: -x[1])

for a in new_diction:
    c = 0
    for b in new_lists:
        if a[0] == b[0]:
            answer.append(b[2])
            c += 1
        if c >= 2:
            c = 0
            break

print(answer)
