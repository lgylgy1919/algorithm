array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []

for command in commands:
    new_array = array[command[0]-1:command[1]]
    new_array = sorted(new_array)
    ans = new_array.pop(command[2]-1)
    answer.append(ans)

print(answer)
