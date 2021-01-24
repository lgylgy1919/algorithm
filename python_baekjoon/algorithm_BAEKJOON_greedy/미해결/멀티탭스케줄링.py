n, k = map(int, input().split())
order = list(map(int, input().split()))

lists = []
nlists = list(order)
an = 0

for i in order:
    lists.append(i)
    lists = list(set(lists))
    del nlists[0]
    if len(lists) > n:
        test = []
        for j in lists:
            a = nlists.count(j)
            test.append(a)
        del test[-1]
        b = min(test)
        c = test.index(b)
        del lists[c]
        an += 1
print(an)

