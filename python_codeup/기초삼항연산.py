# c, d = input().split(" ")
# a = int(c)
# b = int(d)
# result = a if a>b else b
# print(result)

x,y,z = input().split(" ")
a = int(x)
b = int(y)
c = int(z)

result = (a if a<b else b) if (a if a<b else b)<c else c
print(result)