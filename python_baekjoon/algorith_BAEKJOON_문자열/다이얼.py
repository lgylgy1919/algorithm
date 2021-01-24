arr = list(input())
sec = 0
a = ["A", "B", "C"]
b = ["D", "E", "F"]
c = ["G", "H", "I"]
d = ["J", "K", "L"]
e = ["M", "N", "O"]
f = ["P", "Q", "R", "S"]
g = ["T", "U", "V"]
h = ["W", "X", "Y", "Z"]
for i in range(len(arr)):
    if arr[i] in a:
        sec += 3
    elif arr[i] in b:
        sec += 4
    elif arr[i] in c:
        sec += 5
    elif arr[i] in d:
        sec += 6
    elif arr[i] in e:
        sec += 7
    elif arr[i] in f:
        sec += 8
    elif arr[i] in g:
        sec += 9
    else:
        sec += 10
print(sec)
