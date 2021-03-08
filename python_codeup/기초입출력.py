# a,b=input().split(' ')
# print(a,b)

# c,d=input().split(' ')
# print(d,c)

# a = float(input())
# print("%0.2f" %a)

# a = input()
# b = int(a)
# print(b,b,b)

# a,b = input().split(':')
# print(a)
# print(b)
# print(f"{a}:{b}")

# a,b,c = input().split('.')
# a = int(a)
# b = int(b)
# c = int(c)
# print("%02d" %a + "." + "%02d" %b + "." + "%02d" %c)

# a  = input()
# print(a.replace('-',""))

# a = input()
# print(a)

# a ,b = input().split(".")
# print(a)
# print(b)

# a = list(input())
# for char in a:
#     print(f"'{char}'")

 
# num = list(input())
# num1 = int(num[0])*10000
# num2 = int(num[1])*1000
# num3 = int(num[2])*100
# num4 = int(num[3])*10
# num5 = int(num[4])
# print([num1])
# print([num2])
# print([num3])
# print([num4])
# print([num5])

# list = input().split(":")
# print(list[1])

# 2014.06.17 -> 17-06-2015

# list = input().split(".")
# print(f"{list[2]}-{list[1]}-{list[0]}")

# a = float(input())
# print("%0.11f" %a)

word = input()
lists = list(word)
for i in range(len(lists)):
    print(f"'{lists[i]}'")