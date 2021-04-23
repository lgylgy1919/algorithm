gas = [2, 3, 4]
cost = [3, 4, 3]


def canCompleteCircuit(gas, cost):
    margin = []
    for i in range(len(gas)):
        margin.append(gas[i] - cost[i])

    # margin = [-2, -2, -2, 3, 3]

    for i in range(len(margin)):
        sum = 0
        for j in range(len(margin)):
            if i + j < len(margin):
                sum += margin[i + j]
            else:
                sum += margin[i + j - len(margin)]

            if sum < 0:
                break
        if sum >= 0:
            break

    if i == len(margin) - 1 and sum < 0:
        i = -1

    return i


def canCompleteCircuit1(gas, cost):
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)

            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_tarvel = False
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start
    return -1


def canCompleteCircuit2(gas, cost):
    # 모든 주유소 방문 가능 여부 판별
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start


canCompleteCircuit(gas, cost)
