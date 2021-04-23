import bisect

g = [7, 8, 9, 10]
s = [5, 6, 7, 8]
for i in s:
    index = bisect.bisect_right(g, i)
    print(index)