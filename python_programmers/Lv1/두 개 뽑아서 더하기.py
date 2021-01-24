numbers = [5, 0, 2, 7]
result = [2, 3, 4, 5, 6, 7]

sums = []

for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        element = numbers[i] + numbers[j]
        sums.append(element)
    print(sums)


print(sorted(set(sums)))
