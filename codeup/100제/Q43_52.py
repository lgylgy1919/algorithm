# Q43
a, b = map(float, input().split(" "))
c = a / b
print(format(c, ".3f"))

# Q44
a, b = map(int, input().split(" "))
sum = a + b
difference = abs(a - b)
product = a * b
share = a // b
remainder = a % b
divde = format(float(a / b), ".2f")
print(sum, difference, product, share, remainder, divde, sep="\n")

# Q45
a, b, c = map(int, input().split(" "))
sum = a + b + c
average = format(sum / 3, ".2f")
print(sum, average)

# Q46
n = int(input())
print(n << 1)

# Q47
a, b = map(int, input().split(" "))
print(a << b)

# Q48
a, b = map(int, input().split(" "))
print(a < b)

# Q49
a, b = map(int, input().split(" "))
print(a == b)

# Q50
a, b = map(int, input().split(" "))
print(a <= b)

# Q51
a, b = map(int, input().split(" "))
print(a != b)

# Q52
n = int(input())
print(bool(n))
