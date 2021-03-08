strings = ["abce", "abcd", "cdx"]
n = 2

strings = sorted(strings)
strings.sort(key=lambda x: x[n-1])

print(strings)
