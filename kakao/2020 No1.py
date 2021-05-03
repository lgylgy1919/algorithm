def solution(numbers, hand):
    location = [
        [3, 1],
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 0],
        [2, 1],
        [2, 2],
        [3, 0],
        [3, 2],
    ]
    Left = 10
    Right = 11
    answer = ""
    for n in numbers:
        if n in {1, 4, 7}:
            answer += "L"
            Left = n
        elif n in {3, 6, 9}:
            answer += "R"
            Right = n
        else:

            l_dist = (location[n][0] - location[Left][0]) ** 2 + (
                location[n][1] - location[Left][1]
            ) ** 2
            r_dist = (location[n][0] - location[Right][0]) ** 2 + (
                location[n][1] - location[Right][1]
            ) ** 2
            print(l_dist, r_dist)
            if l_dist > r_dist:
                answer += "R"
                Right = n
            elif l_dist < r_dist:
                answer += "L"
                Left = n
            else:
                if hand == "right":
                    answer += "R"
                    Right = n
                else:
                    answer += "L"
                    Left = n

    print(answer)
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "right"

solution(numbers, hand)