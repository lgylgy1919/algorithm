'''
10
10 4 2 3 6 6 7 9 8 5

2
'''
count = int(input())
list = input().split(" ")
a =int(list[0])
for i in range(0,count):
    if (int(list[i])<a):
        a = int(list[i])
print(a)
