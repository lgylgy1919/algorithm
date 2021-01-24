participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = ''
temp = 0
dic = {}

for part in participant:
    dic[hash(part)] = part
    print(dic)
    temp += int(hash(part))
    print(temp)

for com in completion:
    temp -= hash(com)

answer = dic[temp]
print(answer)
