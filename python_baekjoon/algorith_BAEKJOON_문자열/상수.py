"""
a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
a = (int(a[0]) * 100) + (int(a[1]) * 10) + int(a[2])
b.reverse()
b = (int(b[0]) * 100) + (int(b[1]) * 10) + int(b[2])
print(a if a > b else b)
"""
"""
print(max([''.join(reversed(i)) for i in input().split()]))
"""

# print(max(input()[::-1].split()))

print(max(734, 893))
print("453"[::-1])
print(type("453"[::-1]))
print(max(["12", "34"]))
