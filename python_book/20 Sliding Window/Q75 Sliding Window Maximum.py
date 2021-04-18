import collections


def maxSlidingWindow(nums, k):
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max[i : i + k])

    return r


def maxSlidingWindow2(nums, k):
    results = []
    window = collections.deque()
    current_max = float("-inf")
    for i, v in enumerate(nums):
        window.append(v)
        if k < k - 1:
            continue

        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float("-inf"):
            current_max - max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float("-inf")

    return results