# bridge_length = 2
bridge_length = 100
# weight = 10
weight = 100
# truck_weights = [7, 4, 5, 6]
# truck_weights = [10]
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ]

point = len(truck_weights)


on_bridge = []
end_bridge = []
total_time = 0
on_bridge_weight = 0

while len(end_bridge) != point:
    if len(truck_weights) != 0:
        on_bridge.insert(0, truck_weights.pop(0))
        on_bridge_weight += on_bridge[0]

        if on_bridge_weight > weight:
            on_bridge_weight -= on_bridge[0]
            truck_weights.insert(0, on_bridge.pop(0))
            on_bridge.insert(0, "*")

        if len(on_bridge) >= bridge_length:
            if type(on_bridge[-1]) == int:
                end_bridge.insert(0, on_bridge[-1])
                on_bridge_weight -= on_bridge[-1]
            del on_bridge[-1]

    else:
        on_bridge.insert(0, "*")
        if len(on_bridge) > bridge_length:
            if type(on_bridge[-1]) == int:
                end_bridge.insert(0, on_bridge[-1])
                on_bridge_weight -= on_bridge[-1]
                on_bridge.insert(0, "*")
            del on_bridge[-1]

    total_time += 1


print(total_time)
