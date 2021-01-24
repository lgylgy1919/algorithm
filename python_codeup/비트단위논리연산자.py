# a = input()
# b = bin(~int(a)).replace("0b","")
# print(int(b,2))

# a = 0b101011
# b = 0b100110
# c = a&b
# print(type(a))
# print(c)

a, b = input().split(" ")
c = int(a)&int(b)
print(c)
