array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for command in commands:
    new_array = array[command[0] - 1 : command[1]]
    print(new_array)
    answer.append(sorted(new_array)[command[2] - 1])

print(answer)


list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1, commands]))
