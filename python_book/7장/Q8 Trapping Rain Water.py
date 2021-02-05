height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 투포인터 활용


def trap(height):
    if not height:
        return 0

    volume = 0
    left = 0
    right = len(height)-1
    left_max = height[left]
    right_max = height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

        print(volume)
    return volume


# stack으로 풀이


def trap_stack(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


trap(height)
