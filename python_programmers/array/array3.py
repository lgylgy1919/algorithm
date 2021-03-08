citations = [12, 11, 10, 9, 8, 1]
citations.sort(reverse=True)
print(citations)
# [1, 8, 9, 10, 11, 12]
# [12, 11, 10, 9, 8, 1]


s = len(citations)

while True:
    cnt = 0
    for citation in citations:
        if citation >= s:
            cnt += 1
