def solution(n, k, cmd):

    deleted = []
    numbers = {}
    answer = ""

    for i in range(n):
        numbers[i] = "O"

    for c in cmd:
        if len(c) > 1:
            c, m = c.split(" ")

        if c == "U":
            t = 0
            while t < int(m):
                if numbers[k - 1] == "O":
                    t += 1
                k -= 1

        elif c == "D":
            t = 0
            while t < int(m):
                if numbers[k + 1] == "O":
                    t += 1
                k += 1

        elif c == "C":
            numbers[k] = "X"
            deleted.append(k)
            # k가 가장 아래에 있는지 체크
            test = []
            for i in range(k + 1, len(numbers)):
                test.append(numbers[i])
            # 가장 아래가 아닌 경우
            if "O" in test:
                t = 0
                while t < 1:
                    if numbers[k + 1] == "O":
                        t += 1
                    k += 1
            # k가 가장 아래인 경우
            else:
                t = 0
                while t < 1:
                    if numbers[k - 1] == "O":
                        t += 1
                    k -= 1

        else:
            numbers[deleted.pop()] = "O"

        print(numbers, k)

    for number in numbers:
        answer += numbers[number]
    print(answer)
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]

solution(n, k, cmd)
