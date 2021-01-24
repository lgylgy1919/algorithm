numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
hands = ["*", "#"]
answer = []

for n in numbers:
    if n in [1, 4, 7]:
        answer.append("L")
        hands[0] = n
    elif n in [3, 6, 9]:
        answer.append("R")
        hands[1] = n
    elif n in [2, 5, 8, 0]:
        for key in keys:
            if n in key:
                lenl2 = keys.index(key)
        for key in keys:
            if hands[0] in key:
                lenl1 = keys.index(key)

        disl = abs(lenl1-lenl2)

        for key in keys:
            if n in key:
                lenr2 = keys.index(key)
        for key in keys:
            if hands[1] in key:
                lenr1 = keys.index(key)

        disr = abs(lenr1-lenr2)

        if disr > disl:
            hands[0] = n
            answer.append("L")
        elif disr < disl:
            hands[1] = n
            answer.append("R")
        elif disr == disl:
            if hand == "right":
                hands[1] = n
                answer.append("R")
            else:
                hands[0] = n
                answer.append("L")
    print(hands)

print(answer)
