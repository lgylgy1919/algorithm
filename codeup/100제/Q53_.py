# 53
a = bool(int(input()))
print(not a)

# 54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 56
a, b = input().split()
print(((not bool(int(a))) and bool(int(b))) or (bool(int(a)) and (not bool(int(b)))))
