
genres = ["classic", "pop", "classic", "classic", "pop", "song"]
plays = [200, 600, 500, 200, 2500, 30000]
ids = []
for i in range(len(genres)):
    ids.append(i)

answer = []


lists = list(zip(genres, plays, ids))
print(lists)
# lists = [('classic', 200, 0), ('pop', 600, 1), ('classic', 500, 2), ('classic', 200, 3), ('pop', 2500, 4), ('song', 30000, 5)]
new_lists = sorted(lists, key=lambda x: (x[0], -x[1]))
print(new_lists)
# new_lists = [('classic', 500, 2), ('classic', 200, 0), ('classic', 200, 3), ('pop', 2500, 4), ('pop', 600, 1), ('song', 30000, 5)]

'''
장르 순위 구하기
'''
diction = {}
for genre in new_lists:
    if genre[0] in diction:
        a += int(genre[1])
        diction[genre[0]] = a
    else:
        diction[genre[0]] = int(genre[1])
        a = int(genre[1])

print(diction)
# diction = {'classic': 900, 'pop': 3100, 'song': 30000}

new_diction = sorted(diction.items(), key=lambda x: -x[1])
print(new_diction)
# new_diction = [('song', 30000), ('pop', 3100), ('classic', 900)]
# new_lists = [('classic', 500, 2), ('classic', 200, 0), ('classic', 200, 3), ('pop', 2500, 4), ('pop', 600, 1), ('song', 30000, 5)]


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
