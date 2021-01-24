word = list(input())
arr = []
for i in range(97, 123):
    a = 0
    if chr(i) in word:
        for j in range(len(word)):
            if word[j] == chr(i):
                arr.append(a)
                break
            else:
                a += 1
    else:
        arr.append("-1")
for k in range(len(arr)):
    print(arr[k], end=" ")

"""
word = list(input())
for i in range(97, 123):
    if chr(i) in word:
        print(word.index(chr(i)), end=" ")
    else:
        print("-1", end=" ")
"""
"""
word = input()
for i in range(97, 123):
    print(str(word.find(chr(i))), end=" ")
"""
