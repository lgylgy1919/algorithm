string1, string2 = input().split(" ")
list1 = list(string1)
list2 = list(string2)
m = len(list1)
n = len(list2)
f = []
a=0
for i in range(n-m+1):
    k = 0
    for j in range(m):
        if list1[j] != list2[a+j]:
            k+=1
    a+=1
    f.append(k)

print(min(f))
